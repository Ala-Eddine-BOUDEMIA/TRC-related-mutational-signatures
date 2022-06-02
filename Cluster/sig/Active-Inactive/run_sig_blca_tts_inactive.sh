#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=8gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_blca_tts_inactive

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/TTS/inactive
mkdir /local/scratch/mutational_signatures_blca_tts_inactive

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_tts_inactive
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_tts_inactive

source env/bin/activate
python /local/scratch/mutational_signatures_blca_tts_inactive/extract_sigs.py --dataset BLCA --region TTS --num_signatures 7 --cluster --state inactive

cp -r /local/scratch/mutational_signatures_blca_tts_inactive/Mutational_Signatures/BLCA/TTS/inactive/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/TTS/inactive/
rm -r /local/scratch/mutational_signatures_blca_tts_inactive