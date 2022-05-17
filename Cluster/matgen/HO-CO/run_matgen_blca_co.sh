#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca_co

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/co-directional
mkdir /local/scratch/mutational_profiles_blca_co-directional

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_co-directional
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_co-directional

source env/bin/activate
python /local/scratch/mutational_profiles_blca_co-directional/7_matgen.py --dataset BLCA --cluster --region Co-directional

cp -r /local/scratch/mutational_profiles_blca_co-directional/Data/BLCA/Co-directional/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/Co-directional/
rm -r /local/scratch/mutational_profiles_blca_co-directional