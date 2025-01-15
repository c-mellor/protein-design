#!/bin/bash

#SBATCH --job-name=mesotest
#SBATCH --partition=veryshort
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=02:00:00
#SBATCH --mem=6GB
#SBATCH --account=chem023222

module load apps/rosetta/3.12

rosetta_scripts.static.linuxgccrelease @flags -out:prefix ${SLURM_JOBID}_ -out:suffix _${SLURM_ARRAY_TASK_ID}
