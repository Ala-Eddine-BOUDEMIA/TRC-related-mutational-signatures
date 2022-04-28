#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_tts_inactive

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/TTS/inactive
mkdir /local/scratch/mutational_profiles_brca_tts_inactive

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_tts_inactive
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_tts_inactive

source env/bin/activate
python /local/scratch/mutational_profiles_brca_tts_inactive/7_matgen.py --cancer_type BRCA --region TTS --is_active False

cp -r /local/scratch/mutational_profiles_brca_tts_inactive/Data/BRCA/TTS/inactive/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/TTS/inactive/
rm -rf /local/scratch/mutational_profiles_brca_tts_inactive