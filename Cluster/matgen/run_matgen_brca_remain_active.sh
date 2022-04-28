#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_remain_active

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/Remain/active
mkdir /local/scratch/mutational_profiles_brca_remain_active

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_remain_active
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_remain_active

source env/bin/activate
python /local/scratch/mutational_profiles_brca_remain_active/7_matgen.py --cancer_type BRCA --region Remain

cp -r /local/scratch/mutational_profiles_brca_remain_active/Data/BRCA/Remain/active/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/Remain/active/
rm -r /local/scratch/mutational_profiles_brca_remain_active