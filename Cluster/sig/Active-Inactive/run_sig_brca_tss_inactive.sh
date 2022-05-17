#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_tss_inactive

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/TSS/inactive
mkdir /local/scratch/mutational_signatures_brca_tss_inactive

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_tss_inactive
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_tss_inactive

source env/bin/activate
python /local/scratch/mutational_signatures_brca_tss_inactive/8_extract_sigs.py --dataset BRCA --region TSS --num_signatures 4 --cluster

cp -r /local/scratch/mutational_signatures_brca_tss_inactive/Mutational_Signatures/BRCA/TSS/inactive/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/TSS/inactive/
rm -r /local/scratch/mutational_signatures_brca_tss_inactive