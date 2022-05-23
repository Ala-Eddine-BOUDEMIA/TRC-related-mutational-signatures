#!/bin/bash
## Torque Configuration
# resources
#PBS -l walltime=24:00:00
#PBS -l mem=2gb
#PBS -l nodes=1:ppn=2
#PBS -q batch


# Information
#PBS -N matgen_brca_divergent

source /data/tmp/aboudemi/profile.sh

mkdir -p /data/tmp/aboudemi/Mutational_Profiles/BRCA/Divergent
mkdir /local/scratch/mutational_profiles_brca_divergent

cp -r /data/tmp/aboudemi/Data /local/scratch/mutational_profiles_brca_divergent
cp /data/tmp/aboudemi/*.py /local/scratch/mutational_profiles_brca_divergent

source env/bin/activate
python /local/scratch/mutational_profiles_brca_divergent/matgen.py --cluster --region Divergent

cp -r /local/scratch/mutational_profiles_brca_divergent/Data/BRCA/Divergent/output/* /data/tmp/aboudemi/Mutational_Profiles/BRCA/Divergent/
rm -r /local/scratch/mutational_profiles_brca_divergent