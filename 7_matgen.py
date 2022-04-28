from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

import Config

cancer = Config.args.cancer_type
region = Config.args.region

if Config.args.is_active == "True":
	state = "active"
elif Config.args.is_active == "False" :
	state = "inactive"

if Config.args.is_cancer_specific == "False":
	state = "6kb"

if Config.args.cluster == "True":
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		cancer + "_" + region + "_" + state, "GRCh38", 
		
		"/local/scratch/mutational_profiles_" \
			+ cancer.lower() + "_" + region.lower() + "_" + state + "/Data/" \
				+ cancer + "/" + region + "/" + state + "/", 
		
		plot=True)
elif Config.args.cluster == "False":
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		cancer + "_" + region + "_" + state, "GRCh38", 
		"Data/" + cancer + "/" + region + "/" + state + "/", 
		plot=True)