#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=4
#PBS -q batch


# Information
#PBS -N matgen_blca_remain

source /Data/tmp/aboudemi/profile.sh

mkdir /Data/tmp/aboudemi/Mutational_Profiles/BLCA/Remain
mkdir /local/scratch/blca_remain_profiles

cp /Data/tmp/aboudemi/Data/ /local/scratch/blca_remain_profiles
cp /Data/tmp/aboudemi/*.py /local/scratch/blca_remain_profiles

source env/bin/activate
python /local/scratch/blca_remain_profiles/5_matgen.py -c BLCA -r Remain

cp /local/scratch/blca_remain_profiles/Mutational_Profiles/BLCA/Remain /Data/tmp/aboudemi/Mutational_Profiles/BLCA/Remain
rm -r /local/scratch/blca_remain_profiles