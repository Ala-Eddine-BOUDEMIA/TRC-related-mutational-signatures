#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=4
#PBS -q batch


# Information
#PBS -N matgen_blca_remain

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/Remain
mkdir /local/scratch/blca_remain_profiles

cp -r /data/tmp/aboudemi/Data/ /local/scratch/blca_remain_profiles
cp /data/tmp/aboudemi/*.py /local/scratch/blca_remain_profiles

source env/bin/activate
python /local/scratch/blca_remain_profiles/5_matgen.py --cancer_type BLCA --region Remain

cp -r /local/scratch/blca_remain_profiles/Data/BLCA/Remain/6kb/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/Remain/
rm -r /local/scratch/blca_remain_profiles