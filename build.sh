#!/bin/bash
# build.sh — budowanie strony na produkcję


# przejdź do katalogu nadrzędnego (gdzie python_static jest pakietem)
cd "$(dirname "$0")/.."

python3 -m python_static.src.main "/python_static/"