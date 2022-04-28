#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_remain_active

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Remain/active
mkdir /local/scratch/mutational_signatures_brca_remain_active

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_remain_active
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_remain_active

source env/bin/activate
python /local/scratch/mutational_signatures_brca_remain_active/8_extract_sigs.py --cancer_type BRCA --region Remain --num_signatures 4

cp -r /local/scratch/mutational_signatures_brca_remain_active/Mutational_Signatures/BRCA/Remain/active/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Remain/active/
rm -r /local/scratch/mutational_signatures_brca_remain_active