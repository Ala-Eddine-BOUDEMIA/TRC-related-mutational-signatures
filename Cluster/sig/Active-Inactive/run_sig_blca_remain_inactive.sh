#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=8gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_blca_remain_inactive

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/Remain/inactive
mkdir /local/scratch/mutational_signatures_blca_remain_inactive

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_remain_inactive
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_remain_inactive

source env/bin/activate
python /local/scratch/mutational_signatures_blca_remain_inactive/extract_sigs.py --dataset BLCA --region Remain --num_signatures 7 --cluster --state inactive

cp -r /local/scratch/mutational_signatures_blca_remain_inactive/Mutational_Signatures/BLCA/Remain/inactive/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/Remain/inactive/
rm -r /local/scratch/mutational_signatures_blca_remain_inactive