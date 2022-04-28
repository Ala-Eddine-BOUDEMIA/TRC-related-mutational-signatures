from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

import Config

cancer = Config.args.cancer_type
region = Config.args.region
if Config.args.is_active:
	state = "active"
else:
	state = "incative"

if Config.args.is_cancer_specific == False:
	state = "6kb"

if Config.args.cluster:
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		cancer + "_" + region + "_" + state, "GRCh38", 
		
		"/local/scratch/mutational_profiles_" \
			+ cancer.lower() + "_" + region.lower() + "_" + state + "/Data/" \
				+ cancer + "/" + region + "/" + state + "/", 
		
		plot=True)
else:
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		cancer + "_" + region + "_" + state, "GRCh38", 
		"Data/" + cancer + "/" + region + "/" + state + "/", 
		plot=True)