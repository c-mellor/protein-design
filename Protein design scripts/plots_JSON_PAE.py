import os 
import json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

# load languages/anaconda3/2022.11-3.9.13
# soure activate plotting
# run this script
# conda deactivate 

# Set matplotlib backend for writing/creating files not viewing them.
#mpl.use("Agg")

#name="dimer_TSN_name_smcontacts"
dpi=300

def plot_data_from_json_files(directory):
    # Initialize lists to store data for plotting
    #pae_values=[]
    #plddt_values=[]
    
    # Iterate through the JSON files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
                  
            if os.path.isfile(file_path):
                with open(file_path, 'r') as json_file:
                    try:
                        output = {k: np.array(v) for k, v in json.load(json_file).items()}
                        # Assuming your JSON has keys 'x' and 'y'
                        #pae_values.append(output["pae"])
                        #plddt_values.append(output["plddt"])
                    except json.JSONDecodeError as e:
                        print(f"Error reading {filename}: {e}")

           # Plot contact probabilities as a heatmap
            plt.figure(figsize=(8, 6))
            plt.imshow(output["pae"], cmap="bwr")
            plt.title("Predicted Contact Probabilities " + str(filename))
            plt.colorbar(label="Probability")
            plt.xlabel("Residue Index")
            plt.ylabel("Residue Index")
            plt.savefig("PAE_" + str(filename) + ".png", format="png")
            plt.clf()
            
            # Plot plddt scores
            plt.figure(figsize=(6, 6))
            plt.plot(output["plddt"])
            plt.title("PLDDT Scores " + str(filename))
            plt.xlabel("Residue Index")
            plt.ylabel("PLDDT Score")
            plt.xlim(0,output["plddt"].shape[0])
            plt.ylim(0,100)
            plt.grid(False)
            plt.savefig("pLDDT_" + str(filename) + ".png", format="png")
            plt.clf()

directory="."
plot_data_from_json_files(directory)