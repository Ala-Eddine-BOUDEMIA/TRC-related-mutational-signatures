#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca_remain_inactive

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/Remain/inactive
mkdir /local/scratch/mutational_profiles_blca_remain_inactive

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_remain_inactive
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_remain_inactive

source env/bin/activate
python /local/scratch/mutational_profiles_blca_remain_inactive/matgen.py --dataset BLCA --region Remain --cluster

cp -r /local/scratch/mutational_profiles_blca_remain_inactive/Data/BLCA/Remain/inactive/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/Remain/inactive/
rm -r /local/scratch/mutational_profiles_blca_remain_inactive