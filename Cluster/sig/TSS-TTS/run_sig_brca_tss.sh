#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=12gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_tss

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/TSS/6kb
mkdir /local/scratch/mutational_signatures_brca_tss_6kb

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_tss_6kb
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_tss_6kb

source env/bin/activate
python /local/scratch/mutational_signatures_brca_tss_6kb/extract_sigs.py --dataset BRCA --region TSS --state 6kb --num_signatures 5 --cluster

cp -r /local/scratch/mutational_signatures_brca_tss_6kb/Mutational_Signatures/BRCA/TSS/6kb/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/TSS/6kb/
rm -r /local/scratch/mutational_signatures_brca_tss_6kb