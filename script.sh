#!/bin/bash

mime=$(wl-paste --list-types | grep '^image/' | head -n1)

if [ -n "$mime" ]; then
    wl-paste --type "$mime" > tmp
    source .venv/bin/activate
    python ./main.py tmp 
    file="./genericOutput.png"
    mime=$(file --mime-type -b "$file")
    wl-copy --type "$mime" < "$file"
else 
  echo "No image in the clippy"
fi



