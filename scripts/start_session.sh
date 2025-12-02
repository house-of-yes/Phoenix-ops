#!/bin/bash
# start_session.sh — bootstrap Phoenix Ops context for ChatGPT

# Run context loader
python3 ~/Phoenix-ops/core/context_loader.py || exit 1

# Launch your ChatGPT client (replace with whatever you actually use)
# For example, local client or web API wrapper
# python3 ~/Phoenix-ops/client.py
