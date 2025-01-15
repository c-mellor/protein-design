#!/bin/bash
#SBATCH --account=chem023222
#SBATCH --partition=veryshort
#SBATCH --cpus-per-task=14
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --time=06:00:00
#SBATCH --mem=50GB


python run.py \
	--model_type "ligand_mpnn" \
	--pdb_path "./inputs/m4D2_112res.pdb" \
	--out_folder "./outputs/HEB_total_test_proper" \
	--redesigned_residues "A16 A17 A20 A21 A23 A24 A29 A34 A38 A41 A42 A44 A71 A74 A75 A78 A79 A81 A82 A86 A87 A92 A96 A99 A100 A102 A103" \
	--batch_size 250 \
	--checkpoint_path_sc "./model_params/ligandmpnn_sc_v_32_002_16.pt" \
	--pack_side_chains 1 \
	--number_of_packs_per_design 1 \
	--pack_with_ligand_context 1


### before you can run liggy mpnn, you might need to do this:
# pip install dm-tree
# pip install ml-collections