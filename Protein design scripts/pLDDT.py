#module load languages/anaconda3/3.6.5
import os 
import pandas as pd

# Function to calculate the mean pLDDT from a PDB file
def calculate_mean_plddt(pdb_file):
    plddt_values = []
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith("ATOM"):
                # Assuming the pLDDT value is in the penultimate column
                columns = line.split()
                if len(columns) >= 11:
                    try:
                        plddt = float(columns[-2])
                        plddt_values.append(plddt)
                    except ValueError:
                        pass
    
    if plddt_values:
        mean_plddt = sum(plddt_values) / len(plddt_values)
        return mean_plddt
    else:
        return None

# Directory containing your PDB files
pdb_directory = 'biased/ESMFold_biased'

# List of PDB files in the directory
pdb_files = [f for f in os.listdir(pdb_directory) if f.endswith('.pdb')]

# Create a DataFrame to store the results
results = pd.DataFrame(columns=['PDB File', 'Mean pLDDT'])

# Calculate the mean pLDDT for each PDB file
for pdb_file in pdb_files:
    plddt = calculate_mean_plddt(os.path.join(pdb_directory, pdb_file))
    if plddt is not None:
        results = results.append({'PDB File': pdb_file, 'Mean pLDDT': plddt}, ignore_index=True)
        results = results.sort_values(by=['Mean pLDDT'], ascending=False)
    else:
        print(f"No pLDDT values found in {pdb_file}")

# Save the results to a spreadsheet (e.g., CSV)
results.to_csv('pLDDT_results_ESM_e4D2_biased_sorted.csv', index=False)