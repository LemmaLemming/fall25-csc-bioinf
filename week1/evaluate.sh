#!/bin/bash

# This line ensures that the script will exit immediately if a command fails,
# which is very helpful for debugging in CI environments.
set -euxo pipefail

# === PART 1: RUNNING THE ASSEMBLY ===

# Create the output directory if it doesn't exist
mkdir -p week1/test
echo "Test directory created."

# --- Process data1 ---
echo "Processing data1..."
unzip -o week1/data/data1.zip -d week1/data/
{ time python week1/code/python/main.py week1/data/data1 > week1/test/data1.txt; } 2>> week1/test/data1.txt

# --- Process data2 ---
echo "Processing data2..."
unzip -o week1/data/data2.zip -d week1/data/
{ time python week1/code/python/main.py week1/data/data2 > week1/test/data2.txt; } 2>> week1/test/data2.txt

# --- Process data3 ---
echo "Processing data3..."
unzip -o week1/data/data3.zip -d week1/data/
{ time python week1/code/python/main.py week1/data/data3 > week1/test/data3.txt; } 2>> week1/test/data3.txt

# --- Process data4 ---
echo "Processing data4..."
# Increase the stack size limit to prevent recursion errors for this specific dataset
ulimit -s 8192000
unzip -o week1/data/data4.zip -d week1/data/
{ time python week1/code/python/main.py week1/data/data4 > week1/test/data4.txt; } 2>> week1/test/data4.txt

echo "Evaluation complete for all datasets. Now generating report..."


# === PART 2: PARSING RESULTS AND CREATING THE TABLE ===

# Print the header of the results table
printf "Dataset\tLanguage\tRuntime\t\tN50\n"
printf -- "-------------------------------------------------------------------------------------------------------\n"

# Loop through each of the output files
for i in {1..4}
do
  # Define the file path
  file="week1/test/data${i}.txt"

  # --- 1. Extract Runtime ---
  # Grab the last line, find the word "real", and take the time value next to it.
  runtime=$(grep 'real' "$file" | awk '{print $2}')

  # --- 2. Calculate N50 ---
  # Get all the contig lengths from the file (lines that start with a number)
  lengths=$(grep -E '^[0-9]+ ' "$file" | awk '{print $2}')

  # Calculate the total length of all contigs combined
  total_length=$(echo "$lengths" | awk '{s+=$1} END {print s}')

  # The threshold for N50 is 50% of the total length
  half_length=$(echo "$total_length / 2" | bc)

  # Sort the lengths in descending order and find the N50 value
  n50=0
  current_sum=0
  for length in $(echo "$lengths" | sort -rn); do
    current_sum=$((current_sum + length))
    # Once we cross the 50% threshold, the current contig length is our N50
    if (( $(echo "$current_sum >= $half_length" | bc -l) )); then
      n50=$length
      break
    fi
  done

  # --- 3. Print the formatted table row ---
  printf "data%s\tpython\t\t%s\t\t%s\n" "$i" "$runtime" "$n50"
done