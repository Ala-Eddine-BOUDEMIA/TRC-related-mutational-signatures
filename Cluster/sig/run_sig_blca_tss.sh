#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_blca_tss

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/TSS
mkdir /local/scratch/mutational_signatures_BLCA_TSS

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_BLCA_TSS
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_BLCA_TSS

source env/bin/activate
python /local/scratch/mutational_signatures/6_extract_sigs.py --cancer_type BLCA --region TSS --num_signatures 7

cp -r /local/scratch/mutational_signatures_BLCA_TSS/Mutational_Signatures/BLCA/TSS/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/TSS
rm -r /local/scratch/mutational_signatures_BLCA_TSS