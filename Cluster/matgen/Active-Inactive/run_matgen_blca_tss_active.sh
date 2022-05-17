#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca_tss_active

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/TSS/active
mkdir /local/scratch/mutational_profiles_blca_tss_active

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_tss_active
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_tss_active

source env/bin/activate
python /local/scratch/mutational_profiles_blca_tss_active/7_matgen.py --dataset BLCA --region TSS --is_active --cluster

cp -r /local/scratch/mutational_profiles_blca_tss_active/Data/BLCA/TSS/active/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/TSS/active/
rm -r /local/scratch/mutational_profiles_blca_tss_active