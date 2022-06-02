#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=8gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_convergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Convergent/All
mkdir /local/scratch/mutational_signatures_brca_convergent_All

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_convergent_All
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_convergent_All

source env/bin/activate
python /local/scratch/mutational_signatures_brca_convergent_All/extract_sigs.py --dataset BRCA --num_signatures 5 --cluster --region Convergent --state All

cp -r /local/scratch/mutational_signatures_brca_convergent_All/Mutational_Signatures/BRCA/Convergent/All/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Convergent/All/
rm -r /local/scratch/mutational_signatures_brca_convergent_All