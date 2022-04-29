from SigProfilerExtractor import sigpro as sig
from multiprocessing import freeze_support

import Config

if __name__ == '__main__':

	cancer = Config.args.cancer_type
	region = Config.args.region

	if Config.args.is_active == "True":
		state = "active"
	elif Config.args.is_active == "False" :
		state = "inactive"

	if Config.args.is_cancer_specific == "False":
		state = "6kb"

	if Config.args.cluster == "True":
		freeze_support()
		sig.sigProfilerExtractor(
			"matrix", 

			"/local/scratch/mutational_signatures_" \
			+ cancer.lower() + "_" + region.lower() + "_" + state \
			+ "/Mutational_Signatures/" + cancer + "/" + region + "/" + state + "/", 

			"/local/scratch/mutational_signatures_" \
			+ cancer.lower() + "_" + region.lower() + "_" + state \
			+ "/Mutational_Profiles/" + cancer + "/" + region + "/" + state \
			+ "/SBS/" + cancer + "_" + region + "_" + state + ".SBS96.all", 
			
			reference_genome = "GRCh38", opportunity_genome = "GRCh38",
			cpu = -1, context_type = "96", minimum_signatures = 1, 
			maximum_signatures = Config.args.num_signatures)

	elif Config.args.cluster == "False":
		freeze_support()
		sig.sigProfilerExtractor(
			"matrix", 

			"Mutational_Signatures/" + cancer.lower() + "/" + region.lower() + "/" + state, 
			
			"Mutational_Profiles/" + cancer + "/" + region + "/" + state \
			+ "/SBS/" + cancer + "_" + region + "_" + state + ".SBS96.all", 
			
			reference_genome = "GRCh38", opportunity_genome = "GRCh38", 
			cpu = -1, context_type = "96", minimum_signatures = 1, 
			maximum_signatures = Config.args.num_signatures)