#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_blca_co-directional

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/Co-directional/All/
mkdir /local/scratch/mutational_signatures_blca_co-directional_All

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_co-directional_All
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_co-directional_All

source env/bin/activate
python /local/scratch/mutational_signatures_blca_co-directional_All/extract_sigs.py --dataset BLCA --num_signatures 7 --cluster --region Co-directional --state All

cp -r /local/scratch/mutational_signatures_blca_co-directional_All/Mutational_Signatures/BLCA/Co-directional/All/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/Co-directional/All/
rm -r /local/scratch/mutational_signatures_blca_co-directional_All