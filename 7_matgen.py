from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

import Config

dataset = Config.args.dataset
region = Config.args.region

if Config.args.is_active == True:
	state = "active"
elif Config.args.is_active == False :
	state = "inactive"

if Config.args.is_global == True:
	state = "6kb"

if Config.args.cluster == True:
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		dataset + "_" + region + "_" + state, "GRCh38", 	
		"/local/scratch/mutational_profiles_" \
		+ dataset.lower() + "_" + region.lower() + "_" + state + "/Data/" \
		+ dataset + "/" + region + "/" + state + "/", plot=True)

elif Config.args.cluster == False:
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		dataset + "_" + region + "_" + state, "GRCh38", 
		"Data/" + dataset + "/" + region + "/" + state + "/", plot=True)