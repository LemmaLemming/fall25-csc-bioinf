import os
import sys
import zipfile
import subprocess
import time
from pathlib import Path

def run_setup(codon_source_path, binary_output_path):
    """
    Compiles the Codon source code into an optimized native binary.
    This function is called once before the main loop.
    """
    print("INFO: Compiling Codon source into an optimized binary...")
    
    # Ensure the parent directory for the binary exists
    Path(binary_output_path).parent.mkdir(parents=True, exist_ok=True)
    
    compile_command = [
        'codon', 'build', '-release', '-o', binary_output_path, codon_source_path
    ]
    
    try:
        # We capture output here to hide the verbose compilation messages unless there's an error
        process = subprocess.run(
            compile_command,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"INFO: Successfully compiled binary at {binary_output_path}")
    except subprocess.CalledProcessError as e:
        print("="*50)
        print("FATAL: Codon compilation failed!")
        print(f"Command: {' '.join(compile_command)}")
        print(e.stderr)
        print("="*50)
        sys.exit(1) # Exit the script if compilation fails

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
        if line.strip() and line.strip().startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
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
    if total_length == 0:
        return 0
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
    Main function to compile Codon, unzip datasets, run scripts,
    and generate a comparative summary table.
    """
    datasets = ['data1', 'data2', 'data3', 'data4']
    results = []
    
    # --- 1. SETUP: Compile the Codon binary before starting ---
    codon_source_file = 'code/codon/main.codon'
    codon_binary_file = 'code/codon/main_codon_binary' # The new executable
    run_setup(codon_source_file, codon_binary_file)
    
    # --- 2. DEFINE EXECUTABLES: Point Codon to the new binary ---
    executables = [
        {'type': 'python', 'path': 'code/python/main.py'},
        # The path for Codon is now the compiled binary, not the source file
        {'type': 'codon', 'path': codon_binary_file} 
    ]

    os.makedirs('data', exist_ok=True)
    
    for dataset in datasets:
        print(f"INFO: Processing {dataset}...")
        
        # --- 3. UNZIP DATA ---
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
            
            # --- 4. PREPARE & RUN COMMAND (Simplified) ---
            if executable['type'] == 'python':
                command = [sys.executable, executable['path'], data_path]
            else: # For Codon, run the binary directly
                command = [executable['path'], data_path]

            # The ulimit logic is no longer needed and has been removed.
            
            start_time = time.time()
            process = subprocess.run(
                command,
                capture_output=True,
                text=True,
                shell=False # Set to False for better security and portability
            )
            end_time = time.time()

            # --- 5. PROCESS RESULTS ---
            if process.returncode != 0:
                print(f"ERROR: Script failed for {dataset} with {executable['type']}.")
                print(process.stderr)
                continue
            
            runtime_seconds = end_time - start_time
            minutes, seconds = div_mod = divmod(runtime_seconds, 60)
            runtime_str = f"{int(minutes)}:{seconds:05.2f}"

            n50 = calculate_n50(process.stdout)
            
            results.append({
                'Dataset': dataset,
                'Language': executable['type'],
                'Runtime': runtime_str,
                'N50': n50
            })

    # --- 6. PRINT TABLE ---
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