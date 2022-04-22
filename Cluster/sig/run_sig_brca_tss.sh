#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_brca_tss

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/TSS
mkdir /local/scratch/mutational_signatures

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures

source env/bin/activate
python /local/scratch/mutational_signatures/6_extract_sigs.py --cancer_type BRCA --region TSS --num_signatures 4

cp -r /local/scratch/mutational_signatures/Mutational_Signatures/BRCA/TSS/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/TSS
rm -r /local/scratch/mutational_signatures