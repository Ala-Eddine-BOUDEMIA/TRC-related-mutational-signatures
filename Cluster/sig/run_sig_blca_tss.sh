#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_blca_TSS

source /data/tmp/aboudemi/profile.sh

mkdir /data/tmp/aboudemi/Mutational_Signatures/BLCA/TSS
mkdir /local/scratch/blca_TSS_signatures

cp /data/tmp/aboudemi/Data/ /local/scratch/blca_TSS_signatures
cp /data/tmp/aboudemi/*.py /local/scratch/blca_TSS_signatures

source env/bin/activate
python /local/scratch/blca_TSS_signatures/6_extract_sigs.py -c BLCA -r TSS

cp /local/scratch/blca_TSS_profiles/Mutational_Signatures/BLCA/TSS /data/tmp/aboudemi/Mutational_Signatures/BLCA/TSS
rm -r /local/scratch/blca_TSS_signatures