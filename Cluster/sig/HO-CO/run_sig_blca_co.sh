#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_blca_co-directional

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/Co-directional
mkdir /local/scratch/mutational_signatures_blca_co-directional

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_co-directional
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_co-directional

source env/bin/activate
python /local/scratch/mutational_signatures_blca_co-directional/extract_sigs.py --dataset BLCA --num_signatures 7 --cluster --region Co-directional

cp -r /local/scratch/mutational_signatures_blca_co-directional/Mutational_Signatures/BLCA/Co-directional/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/Co-directional/
rm -r /local/scratch/mutational_signatures_blca_co-directional