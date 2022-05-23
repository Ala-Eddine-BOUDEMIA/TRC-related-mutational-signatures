#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_convergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Convergent
mkdir /local/scratch/mutational_signatures_brca_convergent

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_convergent
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_convergent

source env/bin/activate
python /local/scratch/mutational_signatures_brca_convergent/extract_sigs.py --dataset BRCA --num_signatures 4 --cluster --region Convergent

cp -r /local/scratch/mutational_signatures_brca_convergent/Mutational_Signatures/BRCA/Convergent/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Convergent/
rm -r /local/scratch/mutational_signatures_brca_convergent