# Script to run ESMFold on the cluster.
# author Holly Ford, h.ford@bristol.ac.uk

import sys
import torch
import esm
import json
import numpy as np
from scipy.special import softmax

# You need to make a directory in your scratch space for torch hub to reside
# In your scratch space, make a directory .cache/torch/hub
# Paste the path to this directory into the command below
torch.hub.set_dir("/user/home/cm17124/.cache/torch/hub")
#if u run out of space in home, use scratch

def esmfold(fasta_file):
    with open(fasta_file, "r") as seqs:
        model = esm.pretrained.esmfold_v1()
        model.cuda().requires_grad_(False)
        #model = model.eval().cuda()

        # Optionally, uncomment to set a chunk size for axial attention. This can help reduce memory.
        # Lower sizes will have lower memory requirements at the cost of increased speed.
        model.set_chunk_size(128)


        # reads a fasta file into an array
        seqs_array = []
        for element in seqs:
            seqs_array.append(str(element))

        # appends sequences to a sequence array
        clean_seq_array=[]
        for i in range(len(seqs_array)):
            if i % 2:
                clean_seq_array.append(seqs_array[i])

        # appends names to a names array
        clean_name_array=[]
        for i in range(len(seqs_array)):
            if seqs_array[i] not in clean_seq_array:
                clean_name_array.append(seqs_array[i])

        # tidies up the name array
        clean_name_array_final=[]
        for name in clean_name_array:
            clean_name_array_final.append(name[1:-1])

        # tidies up the seq array - to remove hemes and anything else that follows the hemes
        clean_seq_array_final=[]
        for seq in clean_seq_array:
            processed_seq = seq.split('X')[0]
            clean_seq_array_final.append(processed_seq)

        # Multimer prediction can be done with chains separated by ':'

        #defines a function to infer and write a pdb file
        def infer_and_write_result(seq, model, output_file,name):
            with torch.no_grad():
                output = model.infer_pdb(seq)
            with open(output_file, "w") as f:
                f.write(output)
	# convert ESM output to numpy array 
	  output = {k: v.cpu().numpy() for k, v in output.items()}
	  ptm = output["ptm"][0]
	  plddt = output["plddt"][0,:,1].mean()
	  with open("pTM_pLDDT_report.dat", "w") as f:
		f.write(f'ptm: {ptm:.3f} plddt: {plddt:.1f}')
	# extract PAE and pLDDT values from the output
	  contact_probs = (output["aligned_confidence_probs"][0] * np.arange(64)).mean(-1) * 31
	  plddt_scores = output["plddt"][0,:,1]
	# write PAE and pLDDT values to a json file to be plotted
	  with open("scores_" + str(name) + "_smcontacts_lmcontact..json", "w") as f:
	  json.dump({"pae": contact_probs.tolist(), "plddt": plddt_scores.tolist(), "sm_contacts": sm_contacts.tolist(), "lm_contacts": lm_contacts.tolist()}, f)
	
        #loops though the arrays
        for seq, name, in zip(clean_seq_array_final, clean_name_array_final):
            output_file = f"{name}.pdb"
            infer_and_write_result(seq, model, output_file)

       
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <fasta_file>")
        sys.exit(1)
        
    fasta_file = sys.argv[1]
    esmfold(fasta_file)
