#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=4
#PBS -q batch


# Information
#PBS -N matgen_brca_tts

source /Data/tmp/aboudemi/profile.sh

mkdir /Data/tmp/aboudemi/Mutational_Profiles/BRCA/TTS
mkdir /local/scratch/brca_tts_profiles

cp /Data/tmp/aboudemi/Data/ /local/scratch/brca_tts_profiles
cp /Data/tmp/aboudemi/*.py /local/scratch/brca_tts_profiles

source env/bin/activate
python /local/scratch/brca_tts_profiles/5_matgen.py -c BRCA -r TTS

cp /local/scratch/brca_tts_profiles/Mutational_Profiles/BRCA/TTS /Data/tmp/aboudemi/Mutational_Profiles/BRCA/TTS
rm -r /local/scratch/brca_tts_profiles