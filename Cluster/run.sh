#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=10:00:00
#PBS -l mem=16gb
#PBS -l nodes=1:ppn=8
#PBS -q batch


# Information
#PBS -N matgen

source /Data/tmp/aboudemi/profile_to_source.sh
source env/bin/activate
python /Data/tmp/aboudemi/matgen.py
