#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_BRCA_Remain

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/Remain
mkdir /local/scratch/BRCA_Remain_signatures

cp -r /data/tmp/aboudemi/Data/ /local/scratch/BRCA_Remain_signatures
cp /data/tmp/aboudemi/*.py /local/scratch/BRCA_Remain_signatures

source env/bin/activate
python /local/scratch/BRCA_Remain_signatures/6_extract_sigs.py --cancer_type BRCA --region Remain

cp -r /local/scratch/BRCA_Remain_profiles/Mutational_Signatures/BRCA/Remain /data/tmp/aboudemi/Mutational_Signatures/BRCA/Remain
rm -r /local/scratch/BRCA_Remain_signatures