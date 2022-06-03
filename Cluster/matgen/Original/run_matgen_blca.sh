#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/Original/All
mkdir /local/scratch/mutational_profiles_blca_original_All

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_original_All
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_original_All

source env/bin/activate
python /local/scratch/mutational_profiles_blca_original_All/matgen.py --dataset BLCA --state All --region Original --cluster

cp -r /local/scratch/mutational_profiles_blca_original_All/Data/BLCA/Original/All/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/Original/All/
rm -r /local/scratch/mutational_profiles_blca_original_All