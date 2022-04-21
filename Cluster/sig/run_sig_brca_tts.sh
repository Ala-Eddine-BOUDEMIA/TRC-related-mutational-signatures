#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=6gb
#PBS -l nodes=1:ppn=24
#PBS -q batch


# Information
#PBS -N sig_BRCA_TTS

source /Data/tmp/aboudemi/profile.sh

mkdir /Data/tmp/aboudemi/Mutational_Signatures/BRCA/TTS
mkdir /local/scratch/BRCA_TTS_signatures

cp /Data/tmp/aboudemi/Data/ /local/scratch/BRCA_TTS_signatures
cp /Data/tmp/aboudemi/*.py /local/scratch/BRCA_TTS_signatures

source env/bin/activate
python /local/scratch/BRCA_TTS_signatures/6_extract_sigs.py -c BRCA -r TTS

cp /local/scratch/BRCA_TTS_profiles/Mutational_Signatures/BRCA/TTS /Data/tmp/aboudemi/Mutational_Signatures/BRCA/TTS
rm -r /local/scratch/BRCA_TTS_signatures