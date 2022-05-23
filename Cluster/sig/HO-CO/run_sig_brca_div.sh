#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_brca_divergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Divergent
mkdir /local/scratch/mutational_signatures_brca_divergent

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_brca_divergent
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_brca_divergent

source env/bin/activate
python /local/scratch/mutational_signatures_brca_divergent/extract_sigs.py --dataset BRCA --num_signatures 4 --cluster --region Divergent

cp -r /local/scratch/mutational_signatures_brca_divergent/Mutational_Signatures/BRCA/Divergent/* /data/tmp/aboudemi/Mutational_Signatures/BRCA/Divergent/
rm -r /local/scratch/mutational_signatures_brca_divergent