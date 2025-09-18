#!/bin/bash

# This script automates running and evaluating the Python and Codon assemblers.
# It explicitly uses the Python executable from the project's virtual environment
# to ensure the correct dependencies are found.

# Exit immediately if a command exits with a non-zero status.
set -euxo pipefail

# --- Environment Setup ---
# Define the path to the Python executable within the virtual environment.
PYTHON_CMD="./.venv/bin/python3"
# CORRECTED PATH: Point to the main.py script inside the 'python' subdirectory.
CODE_PATH="week1/code/python/main.py"
DATA_DIR="week1/data"

# Check if the virtual environment and required files exist.
if [ ! -f "$PYTHON_CMD" ]; then
    echo "Error: Python executable not found at $PYTHON_CMD"
    echo "Please create and activate the virtual environment: python3 -m venv .venv"
    exit 1
fi
if [ ! -f "$CODE_PATH" ]; then
    echo "Error: Main script not found at $CODE_PATH"
    exit 1
fi

# Create a temporary directory for unzipping data files.
# The 'trap' command ensures this directory is cleaned up when the script exits.
TEMP_DIR=$(mktemp -d)
trap 'rm -rf -- "$TEMP_DIR"' EXIT

# --- Evaluation ---
# Print the header for our results table.
echo -e "Dataset\tLanguage\tRuntime\t\tN50 (20th Contig)"
echo "-------------------------------------------------------------------------------------------------------"

# Loop through all the provided datasets.
for dataset_name in data1 data2 data3 data4
do
    ZIP_FILE="${DATA_DIR}/${dataset_name}.zip"
    if [ ! -f "$ZIP_FILE" ]; then
        echo "Warning: Zip file not found for ${dataset_name}, skipping."
        continue
    fi
    
    # Unzip the data into our temporary directory.
    unzip -q -o "$ZIP_FILE" -d "$TEMP_DIR"
    UNZIPPED_DATA_PATH="${TEMP_DIR}/${dataset_name}"

    # --- Run Python version ---
    start_time_python=$(date +%s)
    # Use the explicit PYTHON_CMD variable to run the script.
    python_output=$($PYTHON_CMD "$CODE_PATH" "$UNZIPPED_DATA_PATH")
    end_time_python=$(date +%s)

    runtime_seconds_python=$((end_time_python - start_time_python))
    runtime_python=$(date -u -d @"${runtime_seconds_python}" +'%H:%M:%S')
    
    # Extract the length of the 20th contig (line starting with "19 ").
    n50_python=$(echo "${python_output}" | grep "^19 " | awk '{print $2}')
    echo -e "${dataset_name}\tpython\t\t${runtime_python}\t${n50_python}"


    # --- Run Codon version ---
    start_time_codon=$(date +%s)
    # Set up the Codon bridge to use the correct Python from our venv
    export CODON_PYTHON=$($PYTHON_CMD -c 'import find_libpython; print(find_libpython.find())')
    codon_output=$(codon run -release "$CODE_PATH" "$UNZIPPED_DATA_PATH")
    end_time_codon=$(date +%s)

    runtime_seconds_codon=$((end_time_codon - start_time_codon))
    runtime_codon=$(date -u -d @"${runtime_seconds_codon}" +'%H:%M:%S')
    
    n50_codon=$(echo "${codon_output}" | grep "^19 " | awk '{print $2}')
    echo -e "${dataset_name}\tcodon\t\t${runtime_codon}\t${n50_codon}"

done

