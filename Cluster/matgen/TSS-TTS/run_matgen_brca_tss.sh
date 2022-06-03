#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_tss

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/TSS/6kb
mkdir /local/scratch/mutational_profiles_brca_tss_6kb

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_tss_6kb
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_tss_6kb

source env/bin/activate
python /local/scratch/mutational_profiles_brca_tss_6kb/matgen.py --dataset BRCA --state 6kb --region TSS --cluster

cp -r /local/scratch/mutational_profiles_brca_tss_6kb/Data/BRCA/TSS/6kb/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/TSS/6kb/
rm -r /local/scratch/mutational_profiles_brca_tss_6kb