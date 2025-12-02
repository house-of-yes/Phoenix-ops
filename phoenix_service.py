#!/usr/bin/env python3
"""
Minimal Phoenix Ops HTTP service for auto-loading canonical context.
"""

import sys
sys.path.insert(0, "/data/data/com.termux/files/home/Phoenix-ops/core")
import pydantic_fix
import pathlib
import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

BASE_DIR = pathlib.Path.home() / "Phoenix-ops"
PHOENIX_OPS = BASE_DIR / "extensions" / "PHOENIX.ops"
MEMORY_STATE = BASE_DIR / "extensions" / "MEMORY.state"

# -------------------- Utility --------------------

def run_phoenix_ops():
    if not PHOENIX_OPS.exists():
        raise FileNotFoundError(f"{PHOENIX_OPS} not found")
    try:
        result = subprocess.run(
            [str(PHOENIX_OPS)], capture_output=True, text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"PHOENIX.ops failed: {result.stderr}")
    except Exception as e:
        raise RuntimeError(f"Exception running PHOENIX.ops: {e}")

# -------------------- API Endpoints --------------------

@app.get("/load_context")
def load_context():
    try:
        run_phoenix_ops()
        if not MEMORY_STATE.exists():
            raise FileNotFoundError(f"{MEMORY_STATE} not found")
        return PlainTextResponse(MEMORY_STATE.read_text())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status")
def status():
    return {"status": "alive", "phoenix_ops_exists": PHOENIX_OPS.exists()}

# -------------------- Main --------------------

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8765)
