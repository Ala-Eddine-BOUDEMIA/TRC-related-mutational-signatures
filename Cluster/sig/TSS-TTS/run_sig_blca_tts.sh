#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=240:00:00
#PBS -l mem=12gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_blca_tts

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/BLCA/TTS/6kb
mkdir /local/scratch/mutational_signatures_blca_tts_6kb

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_tts_6kb
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_tts_6kb

source env/bin/activate
python /local/scratch/mutational_signatures_blca_tts_6kb/extract_sigs.py --dataset BLCA --region TTS --state 6kb --num_signatures 7 --cluster

cp -r /local/scratch/mutational_signatures_blca_tts_6kb/Mutational_Signatures/BLCA/TTS/6kb/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/TTS/6kb/
rm -r /local/scratch/mutational_signatures_blca_tts_6kb