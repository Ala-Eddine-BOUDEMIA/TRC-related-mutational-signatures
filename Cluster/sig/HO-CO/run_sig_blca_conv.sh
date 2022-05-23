#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_blca_convergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/Convergent
mkdir /local/scratch/mutational_signatures_blca_convergent

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_convergent
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_convergent

source env/bin/activate
python /local/scratch/mutational_signatures_blca_convergent/extract_sigs.py --dataset BLCA --num_signatures 7 --cluster --region Convergent

cp -r /local/scratch/mutational_signatures_blca_convergent/Mutational_Signatures/BLCA/Convergent/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/Convergent/
rm -r /local/scratch/mutational_signatures_blca_convergent