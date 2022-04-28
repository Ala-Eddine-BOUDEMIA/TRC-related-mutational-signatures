#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_tts_active

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/TTS/active
mkdir /local/scratch/mutational_profiles_brca_tts_active

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_tts_active
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_tts_active

source env/bin/activate
python /local/scratch/mutational_profiles_brca_tts_active/7_matgen.py --cancer_type BRCA --region TTS

cp -r /local/scratch/mutational_profiles_brca_tts_active/Data/BRCA/TTS/active/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/TTS/active/
rm -r /local/scratch/mutational_profiles_brca_tts_active