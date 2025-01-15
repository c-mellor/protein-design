#!/bin/bash
#SBATCH --nodes=1
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --time=3-00:00:00
#SBATCH --mem=50GB
#SBATCH --output=esmfold.out
#SBATCH --account=chem023222
 
module purge
module load libs/fair-esm/2.0.0-python3.9.5
date
python esmfold_batch_score_plots_ext.py final_6_designs.fa
date