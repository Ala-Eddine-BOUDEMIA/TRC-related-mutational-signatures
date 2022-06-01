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
mkdir /local/scratch/mutational_signatures_blca_tts

cp -r /data/tmp/aboudemi/Mutational_Profiles /local/scratch/mutational_signatures_blca_tts
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_blca_tts

source env/bin/activate
python /local/scratch/mutational_signatures_blca_tts/extract_sigs.py --dataset BLCA --region TTS --state 6kb --num_signatures 7 --cluster

cp -r /local/scratch/mutational_signatures_blca_tts/Mutational_Signatures/BLCA/TTS/6kb/* /data/tmp/aboudemi/Mutational_Signatures/BLCA/TTS/6kb/
rm -r /local/scratch/mutational_signatures_blca_tts