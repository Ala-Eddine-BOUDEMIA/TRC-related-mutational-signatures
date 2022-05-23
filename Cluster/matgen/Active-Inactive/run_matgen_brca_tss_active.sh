#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_tss_active

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/TSS/active
mkdir /local/scratch/mutational_profiles_brca_tss_active

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_tss_active
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_tss_active

source env/bin/activate
python /local/scratch/mutational_profiles_brca_tss_active/matgen.py --dataset BRCA --region TSS --is_active --cluster

cp -r /local/scratch/mutational_profiles_brca_tss_active/Data/BRCA/TSS/active/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/TSS/active/
rm -r /local/scratch/mutational_profiles_brca_tss_active