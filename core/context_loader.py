#!/usr/bin/env python3
"""
Phoenix Ops auto-loader: reconstitutes canonical context and enforces standing rules.
"""

print("[DEBUG] context_loader.py started")

import pathlib
import subprocess
import sys

# Path to Phoenix Ops script or executable
PHOENIX_OPS_PATH = pathlib.Path(__file__).parent.parent / "extensions" / "PHOENIX.ops"

def run_phoenix_ops():
    """Invoke PHOENIX.ops to restore canonical context and enforce rules."""
    if not PHOENIX_OPS_PATH.exists():
        print(f"[ERROR] PHOENIX.ops not found at {PHOENIX_OPS_PATH}", file=sys.stderr)
        sys.exit(1)
    try:
        # Using subprocess to execute PHOENIX.ops
        result = subprocess.run([str(PHOENIX_OPS_PATH)], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[ERROR] PHOENIX.ops failed:\n{result.stderr}", file=sys.stderr)
            sys.exit(result.returncode)
        print(result.stdout)
    except Exception as e:
        print(f"[ERROR] Exception running PHOENIX.ops: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_phoenix_ops()
    print("[DEBUG] context_loader.py executed")
