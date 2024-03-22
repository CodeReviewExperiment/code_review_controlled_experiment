#!/bin/bash

find /home/cr-study-2024 -type f -path "/home/cr-study-2024/dev*/cr-study-2024/*/*/README.md" | while read -r file; do
    echo "File: $file"
    tail -n 2 "$file"
    echo
    echo "---------------------"
done
