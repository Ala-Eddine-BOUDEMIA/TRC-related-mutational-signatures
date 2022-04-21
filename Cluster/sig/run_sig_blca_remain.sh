#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_blca_remain

source /data/tmp/aboudemi/profile.sh

mkdir /data/tmp/aboudemi/Mutational_Signatures/BLCA/Remain
mkdir /local/scratch/blca_remain_signatures

cp /data/tmp/aboudemi/Data/ /local/scratch/blca_remain_signatures
cp /data/tmp/aboudemi/*.py /local/scratch/blca_remain_signatures

source env/bin/activate
python /local/scratch/blca_remain_signatures/6_extract_sigs.py -c BLCA -r Remain

cp /local/scratch/blca_remain_profiles/Mutational_Signatures/BLCA/Remain /data/tmp/aboudemi/Mutational_Signatures/BLCA/Remain
rm -r /local/scratch/blca_remain_signatures