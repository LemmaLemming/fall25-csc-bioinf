import os
import sys
import zipfile
import subprocess
import time

def calculate_n50(output_text):
    """
    Parses the text output from the assembly process to calculate the N50 value.
    N50 is the length of the shortest contig in the set that contains at least
    50% of the total assembly length.
    """
    contig_lengths = []
    # Iterate through each line of the provided text output
    for line in output_text.strip().split('\n'):
        # A valid line starts with a digit and contains contig information
        if line.strip() and line.strip()[0].isdigit():
            parts = line.split()
            # Ensure the line has the expected format (e.g., "ID Length")
            if len(parts) >= 2:
                try:
                    # The second part should be the contig length
                    contig_lengths.append(int(parts[1]))
                except (ValueError, IndexError):
                    # Ignore lines with non-integer lengths
                    continue
    
    # If no contigs were found, N50 is 0
    if not contig_lengths:
        return 0

    # Calculate the total length of all contigs
    total_length = sum(contig_lengths)
    half_length = total_length / 2.0
    
    # Sort contigs from longest to shortest
    sorted_lengths = sorted(contig_lengths, reverse=True)
    
    # Find the contig length that crosses the 50% threshold
    cumulative_sum = 0
    for length in sorted_lengths:
        cumulative_sum += length
        if cumulative_sum >= half_length:
            return length
            
    return 0 # Failsafe return

def main():
    """
    Main function to unzip datasets, run Python and Codon scripts,
    and generate a comparative summary table.
    """
    datasets = ['data1', 'data2', 'data3', 'data4']
    results = []
    
    # Define the executables to compare
    executables = [
        {'type': 'python', 'path': 'code/python/main.py'},
        {'type': 'codon', 'path': 'code/codon/main.codon'}
    ]

    # Ensure the target directory for unzipping exists
    os.makedirs('data', exist_ok=True)
    
    for dataset in datasets:
        print(f"INFO: Processing {dataset}...")
        
        # --- 1. Unzip the data ---
        zip_path = os.path.join('data', f'{dataset}.zip')
        data_path = os.path.join('data', dataset)
        
        if os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall('data/')
        else:
            print(f"WARNING: Zip file not found for {dataset} at {zip_path}")
            continue
            
        for executable in executables:
            print(f"  -> Running {executable['type']}...")
            
            # --- 2. Prepare the command ---
            if executable['type'] == 'python':
                # Use sys.executable to ensure we use the same Python interpreter running this script
                command = [sys.executable, executable['path'], data_path]
            else: # For Codon
                command = ['codon', 'run', executable['path'], data_path]

            # Special case for data4: increase stack size limit using a shell
            if dataset == 'data4':
                # Join the command list into a string to be run by the shell
                shell_command = f"ulimit -s 8192000; {' '.join(command)}"
                use_shell = True
            else:
                shell_command = command
                use_shell = False

            # --- 3. Run the subprocess and time it ---
            start_time = time.time()
            process = subprocess.run(
                shell_command,
                capture_output=True,
                text=True,
                shell=use_shell
            )
            end_time = time.time()

            # --- 4. Process the results ---
            if process.returncode != 0:
                print(f"ERROR: Script failed for {dataset} with {executable['type']}.")
                print(process.stderr)
                continue
            
            runtime_seconds = end_time - start_time
            minutes, seconds = divmod(runtime_seconds, 60)
            runtime_str = f"{int(minutes)}:{seconds:05.2f}"

            n50 = calculate_n50(process.stdout)
            
            # --- 5. Store results ---
            results.append({
                'Dataset': dataset,
                'Language': executable['type'],
                'Runtime': runtime_str,
                'N50': n50
            })

    # --- 6. Print the final, formatted table ---
    print("\n" + "="*50)
    header_format = "%-10s %-10s %-15s %-10s"
    row_format = "%-10s %-10s %-15s %-10d"
    
    print(header_format % ("Dataset", "Language", "Runtime", "N50"))
    print("-" * 50)
    
    for res in results:
        print(row_format % (res['Dataset'], res['Language'], res['Runtime'], res['N50']))
    print("="*50)

if __name__ == "__main__":
    main()