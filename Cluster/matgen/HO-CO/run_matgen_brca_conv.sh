#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_convergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/Convergent
mkdir /local/scratch/mutational_profiles_brca_convergent

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_convergent
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_convergent

source env/bin/activate
python /local/scratch/mutational_profiles_brca_convergent/7_matgen.py --cluster --region Convergent

cp -r /local/scratch/mutational_profiles_brca_convergent/Data/BRCA/Convergent/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/Convergent/
rm -r /local/scratch/mutational_profiles_brca_convergent