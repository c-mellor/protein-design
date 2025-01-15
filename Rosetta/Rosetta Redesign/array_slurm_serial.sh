#!/bin/bash

#SBATCH --job-name=deu_relax
#SBATCH --account=chem023222
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=3-00:0:00
#SBATCH --mem=6GB
#SBATCH --array=1-20

module load apps/rosetta/3.12

rosetta_scripts.static.linuxgccrelease @flags -out:suffix ${SLURM_ARRAY_TASK_ID} -out:prefix $SLURM_JOBID -out:file:silent struct_50_$SLURM_ARRAY_TASK_ID

