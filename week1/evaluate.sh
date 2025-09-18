#!/bin/bash

# This line ensures that the script will exit immediately if a command fails
set -euxo pipefail

# Navigate to the data directory and unzip the data1.zip file
# The -o flag overwrites files without prompting
unzip -o week1/data/data1.zip -d week1/data/

# Create the test directory if it doesn't exist
mkdir -p week1/test

# Run the main.py script with the unzipped data1 directory as an argument
# The output of the script is redirected to a new file in the week1/test directory
python week1/code/main.py week1/data/data1 > week1/test/data1.txt

echo "Evaluation complete. Output stored in week1/test/data1.txt"