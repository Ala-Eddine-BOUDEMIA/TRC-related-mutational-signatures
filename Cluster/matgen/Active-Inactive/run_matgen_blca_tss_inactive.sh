#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca_tss_inactive

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/TSS/inactive
mkdir /local/scratch/mutational_profiles_blca_tss_inactive

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_tss_inactive
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_tss_inactive

source env/bin/activate
python /local/scratch/mutational_profiles_blca_tss_inactive/matgen.py --dataset BLCA --region TSS --cluster

cp -r /local/scratch/mutational_profiles_blca_tss_inactive/Data/BLCA/TSS/inactive/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/TSS/inactive/
rm -r /local/scratch/mutational_profiles_blca_tss_inactive