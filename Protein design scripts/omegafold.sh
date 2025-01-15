#!/bin/bash
#SBATCH --nodes=1
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --time=6:00:00
#SBATCH --mem=10000M
#SBATCH --output=biased_omega.out
#SBATCH --account=chem023222

module add languages/anaconda3/2020-3.8.5 
source activate omegafold
omegafold OmegaFold_biased/e4D2_biased_fold.fa OmegaFold_biased/