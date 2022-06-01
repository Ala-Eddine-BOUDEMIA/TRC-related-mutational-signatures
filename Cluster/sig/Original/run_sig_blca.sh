#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=500:00:00
#PBS -l mem=12gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_blca_original

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/Original
mkdir /local/scratch/mutational_signatures_blca_original_All

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_original_All
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_original_All

source env/bin/activate
python /local/scratch/mutational_signatures_blca_original_All/extract_sigs.py --dataset BLCA --num_signatures 7 --cluster --region Original --state All

cp -r /local/scratch/mutational_signatures_blca_original_All/Mutational_Signatures/BLCA/Original/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/Original/
rm -r /local/scratch/mutational_signatures_blca_original_All