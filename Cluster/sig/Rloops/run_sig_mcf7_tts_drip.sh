#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=72:00:00
#PBS -l mem=16gb
#PBS -l nodes=1:ppn=12
#PBS -q batch


# Information
#PBS -N sig_mcf7_drip_tts

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Signatures/MCF7/TTS/E2-2h/DRIP
mkdir -p /local/scratch/mutational_signatures_mcf7_tts_E2-2h/Mutational_Profiles/MCF7/TTS/E2-2h

cp -r /data/tmp/aboudemi/Mutational_Profiles/MCF7/TTS/E2-2h/output/* /local/scratch/mutational_signatures_mcf7_tts_E2-2h/Mutational_Profiles/MCF7/TTS/E2-2h/
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_signatures_mcf7_tts_E2-2h

source env/bin/activate
python /local/scratch/mutational_signatures_mcf7_tts_E2-2h/extract_sigs.py --dataset MCF7 --region TTS --state E2-2h --num_signatures 5 --cluster 

cp -r /local/scratch/mutational_signatures_mcf7_tts_E2-2h/Mutational_Signatures/MCF7/TTS/E2-2h/* /data/tmp/aboudemi/Mutational_Signatures/MCF7/TTS/E2-2h/DRIP/
rm -r /local/scratch/mutational_signatures_mcf7_tts_E2-2h