#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=4
#PBS -q batch


# Information
#PBS -N matgen_brca_tss

source /Data/tmp/aboudemi/profile.sh

mkdir /Data/tmp/aboudemi/Mutational_Profiles/BRCA/TSS
mkdir /local/scratch/brca_tss_profiles

cp /Data/tmp/aboudemi/Data/ /local/scratch/brca_tss_profiles
cp /Data/tmp/aboudemi/*.py /local/scratch/brca_tss_profiles

source env/bin/activate
python /local/scratch/brca_tss_profiles/5_matgen.py -c BRCA -r TSS

cp /local/scratch/brca_tss_profiles/Mutational_Profiles/BRCA/TSS /Data/tmp/aboudemi/Mutational_Profiles/BRCA/TSS
rm -r /local/scratch/brca_tss_profiles