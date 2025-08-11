#!/bin/bash
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <absolute path to repo folder>"
  echo "Example: $0 /home/debian/gpt4all"
  exit 1
fi
uv run gilot log $1 --full | uv run gilot hotgraph
