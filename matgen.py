from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

import Config

dataset = Config.args.dataset
region = Config.args.region
state = Config.args.state

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