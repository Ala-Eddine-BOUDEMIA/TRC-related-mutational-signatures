#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_blca_convergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BLCA/Convergent
mkdir /local/scratch/mutational_profiles_blca_convergent

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_blca_convergent
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_blca_convergent

source env/bin/activate
python /local/scratch/mutational_profiles_blca_convergent/matgen.py --dataset BLCA --cluster --region Convergent

cp -r /local/scratch/mutational_profiles_blca_convergent/Data/BLCA/Convergent/output/* /data/tmp/aboudemi/Mutational_Profiles/BLCA/Convergent/
rm -r /local/scratch/mutational_profiles_blca_convergent