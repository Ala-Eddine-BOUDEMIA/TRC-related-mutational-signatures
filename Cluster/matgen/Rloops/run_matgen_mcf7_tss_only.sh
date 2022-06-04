#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_mcf7_tss_only

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/MCF7/TSS/E2-2h
mkdir /local/scratch/mutational_profiles_mcf7_tss_E2-2h
mkdir -p /local/scratch/mutational_profiles_mcf7_tss_E2-2h/Data/MCF7/TSS/E2-2h/

cp /data/tmp/aboudemi/Data/MCF7/TSS/E2-2h/only_tss_mutations.maf /local/scratch/mutational_profiles_mcf7_tss_E2-2h/Data/MCF7/TSS/E2-2h/
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_mcf7_tss_E2-2h

source env/bin/activate
python /local/scratch/mutational_profiles_mcf7_tss_E2-2h/matgen.py --dataset MCF7 --region TSS --state E2-2h --cluster

cp -r /local/scratch/mutational_profiles_mcf7_tss_E2-2h/Data/MCF7/TSS/E2-2h/output/* /data/tmp/aboudemi/Mutational_Profiles/MCF7/TSS/E2-2h/
rm -rf /local/scratch/mutational_profiles_mcf7_tss_E2-2h