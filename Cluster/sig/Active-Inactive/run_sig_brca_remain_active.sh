#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=8gb
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
python /local/scratch/mutational_signatures_brca_remain_active/extract_sigs.py --dataset BRCA --region Remain --num_signatures 5 --state active --cluster

cp -r /local/scratch/mutational_signatures_brca_remain_active/Mutational_Signatures/BRCA/Remain/active/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Remain/active/
rm -r /local/scratch/mutational_signatures_brca_remain_active