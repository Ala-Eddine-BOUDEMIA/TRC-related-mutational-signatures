#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_BRCA_TTS

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BRCA/TTS
mkdir /local/scratch/BRCA_TTS_signatures

cp /data/tmp/aboudemi/Data/ /local/scratch/BRCA_TTS_signatures
cp /data/tmp/aboudemi/*.py /local/scratch/BRCA_TTS_signatures

source env/bin/activate
python /local/scratch/BRCA_TTS_signatures/6_extract_sigs.py --cancer_type BRCA --region TTS

cp /local/scratch/BRCA_TTS_profiles/Mutational_Signatures/BRCA/TTS /data/tmp/aboudemi/Mutational_Signatures/BRCA/TTS
rm -r /local/scratch/BRCA_TTS_signatures