#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca_divergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/Divergent
mkdir /local/scratch/mutational_profiles_blca_divergent

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_divergent
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_divergent

source env/bin/activate
python /local/scratch/mutational_profiles_blca_divergent/matgen.py --dataset BLCA --cluster --region Divergent

cp -r /local/scratch/mutational_profiles_blca_divergent/Data/BLCA/Divergent/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/Divergent/
rm -r /local/scratch/mutational_profiles_blca_divergent