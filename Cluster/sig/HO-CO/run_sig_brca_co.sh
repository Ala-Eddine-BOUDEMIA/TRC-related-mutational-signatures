#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_co-directional

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Co-directional
mkdir /local/scratch/mutational_signatures_brca_co-directional

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_co-directional
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_co-directional

source env/bin/activate
python /local/scratch/mutational_signatures_brca_co-directional/extract_sigs.py --dataset BRCA --num_signatures 4 --cluster --region Co-directional

cp -r /local/scratch/mutational_signatures_brca_co-directional/Mutational_Signatures/BRCA/Co-directional/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Co-directional/
rm -r /local/scratch/mutational_signatures_brca_co-directional