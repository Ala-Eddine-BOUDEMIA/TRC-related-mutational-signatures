#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_co

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/Co-directional
mkdir /local/scratch/mutational_profiles_brca_co-directional

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_co-directional
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_co-directional

source env/bin/activate
python /local/scratch/mutational_profiles_brca_co-directional/7_matgen.py --cluster --region Co-directional

cp -r /local/scratch/mutational_profiles_brca_co-directional/Data/BRCA/Co-directional/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/Co-directional/
rm -rf /local/scratch/mutational_profiles_brca_co-directional