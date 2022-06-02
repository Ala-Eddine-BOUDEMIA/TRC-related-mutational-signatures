#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_divergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Divergent/All
mkdir /local/scratch/mutational_signatures_brca_divergent_All

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_divergent_All
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_divergent_All

source env/bin/activate
python /local/scratch/mutational_signatures_brca_divergent_All/extract_sigs.py --dataset BRCA --num_signatures 5 --cluster --region Divergent --state All

cp -r /local/scratch/mutational_signatures_brca_divergent_All/Mutational_Signatures/BRCA/Divergent/All/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Divergent/All/
rm -r /local/scratch/mutational_signatures_brca_divergent_All