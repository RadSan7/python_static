#!/bin/bash
# build.sh — budowanie strony na produkcję

REPO_NAME="python_static"

# przejdź do katalogu nadrzędnego (gdzie python_static jest pakietem)
cd "$(dirname "$0")/.."

python3 -m python_static.src.main "/$REPO_NAME/"