from SigProfilerExtractor import sigpro as sig
from multiprocessing import freeze_support

import Config

if __name__ == '__main__':

	cancer = Config.args.cancer_type
	region = Config.args.region

	freeze_support()
	if Config.args.cluster:
		sig.sigProfilerExtractor("matrix", "/local/scratch/mutational_signatures/Mutational_Signatures/" + cancer + "/" + region + "/6kb", 
			"local/scratch/mutational_signatures/Mutational_Profiles/" + cancer + "/Remain/SBS/" + cancer + "_" + region + "_6kb.SBS96.all", 
			reference_genome = "GRCh38", opportunity_genome = "GRCh38", cpu = -1,
			context_type = "96", minimum_signatures = 1, maximum_signatures = Config.args.num_signatures)
	else:
		sig.sigProfilerExtractor("matrix", "Mutational_Signatures/" + cancer + "/" + region + "/6kb", 
			"Mutational_Profiles/" + cancer + "/Remain/6kb/SBS/" + cancer + "_" + region + "_6kb.SBS96.all", 
			reference_genome = "GRCh38", opportunity_genome = "GRCh38", cpu = -1,
			context_type = "96", minimum_signatures = 1, maximum_signatures = Config.args.num_signatures)