#!/bin/bash

# Navigate to the directory containing the Python scripts
cd "$(dirname "$0")"

# Find and execute all Python scripts in the repository
for script in $(find . -name "*.py"); do
    echo "Executing $script"
    python "$script"
done