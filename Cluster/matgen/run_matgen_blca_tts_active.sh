#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca_tts_active

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/TTS/active
mkdir /local/scratch/mutational_profiles_blca_tts_active

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_tts_active
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_tts_active

source env/bin/activate
python /local/scratch/mutational_profiles_blca_tts_active/7_matgen.py --cancer_type BLCA --region TTS

cp -r /local/scratch/mutational_profiles_blca_tts_active/Data/BLCA/TTS/active/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/TTS/active/
rm -r /local/scratch/mutational_profiles_blca_tts_active