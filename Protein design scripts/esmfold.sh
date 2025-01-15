#!/bin/bash
#SBATCH --nodes=1
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --time=3-00:00:00
#SBATCH --mem=50GB
#SBATCH --output=esmfold_e4D2_biased.out
#SBATCH --account=chem023222

module purge
module load libs/fair-esm/2.0.0-python3.9.5
python esmfold.py ESMFold_biased/e4D2_biased_fold.fa
