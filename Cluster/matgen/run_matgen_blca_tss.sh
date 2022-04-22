#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=4
#PBS -q batch


# Information
#PBS -N matgen_blca_tss

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/TSS/6kb
mkdir /local/scratch/mutational_profiles

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles

source env/bin/activate
python /local/scratch/mutational_profiles/5_matgen.py --cancer_type BLCA --region TSS

cp -r /local/scratch/mutational_profiles/Data/BLCA/TSS/6kb/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/TSS/6kb/
rm -r /local/scratch/mutational_profiles