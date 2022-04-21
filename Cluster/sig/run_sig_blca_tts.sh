#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_blca_TTS

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/TTS
mkdir /local/scratch/blca_TTS_signatures

cp -r /data/tmp/aboudemi/Data/ /local/scratch/blca_TTS_signatures
cp /data/tmp/aboudemi/*.py /local/scratch/blca_TTS_signatures

source env/bin/activate
python /local/scratch/blca_TTS_signatures/6_extract_sigs.py --cancer_type BLCA --region TTS

cp -r /local/scratch/blca_TTS_profiles/Mutational_Signatures/BLCA/TTS /data/tmp/aboudemi/Mutational_Signatures/BLCA/TTS
rm -r /local/scratch/blca_TTS_signatures