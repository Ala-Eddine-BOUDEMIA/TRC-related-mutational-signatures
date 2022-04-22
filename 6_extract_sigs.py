from SigProfilerExtractor import sigpro as sig
from multiprocessing import freeze_support

import Config

if __name__ == '__main__':

	cancer = Config.args.cancer_type
	region = Config.args.region

	if Config.args.cluster:
		freeze_support()
		sig.sigProfilerExtractor("matrix", "/local/scratch/mutational_signatures/Mutational_Signatures/" + cancer + "/" + region + "/6kb/", 
			"/local/scratch/mutational_signatures/Mutational_Profiles/" + cancer + "/" + region + "/SBS/" + cancer + "_" + region + "_6kb.SBS96.all", 
			reference_genome = "GRCh38", opportunity_genome = "GRCh38", cpu = -1, context_type = "96", minimum_signatures = 1, 
			maximum_signatures = Config.args.num_signatures)
	else:
		freeze_support()
		sig.sigProfilerExtractor("matrix", "Mutational_Signatures/" + cancer + "/" + region + "/6kb", 
			"Mutational_Profiles/" + cancer + "/" + region + "/6kb/SBS/" + cancer + "_" + region + "_6kb.SBS96.all", 
			reference_genome = "GRCh38", opportunity_genome = "GRCh38", cpu = -1, context_type = "96", 
			minimum_signatures = 1, maximum_signatures = Config.args.num_signatures)