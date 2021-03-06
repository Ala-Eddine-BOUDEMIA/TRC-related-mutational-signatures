from SigProfilerExtractor import sigpro as sig
from multiprocessing import freeze_support

import Config

if __name__ == '__main__':

	dataset = Config.args.dataset
	region = Config.args.region
	state = Config.args.state

	if Config.args.cluster == True:
		freeze_support()
		sig.sigProfilerExtractor(
			"matrix", 

			"/local/scratch/mutational_signatures_" \
			+ dataset.lower() + "_" + region.lower() + "_" + state \
			+ "/Mutational_Signatures/" + dataset + "/" + region + "/" + state + "/", 

			"/local/scratch/mutational_signatures_" \
			+ dataset.lower() + "_" + region.lower() + "_" + state \
			+ "/Mutational_Profiles/" + dataset + "/" + region + "/" + state \
			+ "/SBS/" + dataset + "_" + region + "_" + state + ".SBS96.all", 
			
			reference_genome = "GRCh38", opportunity_genome = "GRCh38", nmf_replicates = 500,
			cpu = -1, context_type = "96", minimum_signatures = 1, exome = True,
			maximum_signatures = Config.args.num_signatures)

	elif Config.args.cluster == False:
		freeze_support()
		sig.sigProfilerExtractor(
			"matrix", 

			"Mutational_Signatures/" + dataset.lower() + "/" + region.lower() + "/" + state, 
			
			"Mutational_Profiles/" + dataset + "/" + region + "/" + state \
			+ "/SBS/" + dataset + "_" + region + "_" + state + ".SBS96.all", 
			
			reference_genome = "GRCh38", opportunity_genome = "GRCh38", 
			cpu = -1, context_type = "96", minimum_signatures = 1, 
			maximum_signatures = Config.args.num_signatures)