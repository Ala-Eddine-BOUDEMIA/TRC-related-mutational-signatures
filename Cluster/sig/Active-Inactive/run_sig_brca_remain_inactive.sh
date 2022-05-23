#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_remain_inactive

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Remain/inactive
mkdir /local/scratch/mutational_signatures_brca_remain_inactive

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_remain_inactive
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_remain_inactive

source env/bin/activate
python /local/scratch/mutational_signatures_brca_remain_inactive/extract_sigs.py --dataset BRCA --region Remain --num_signatures 4 --cluster

cp -r /local/scratch/mutational_signatures_brca_remain_inactive/Mutational_Signatures/BRCA/Remain/inactive/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Remain/inactive/
rm -r /local/scratch/mutational_signatures_brca_remain_inactive