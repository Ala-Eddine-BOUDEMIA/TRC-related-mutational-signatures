from SigProfilerExtractor import sigpro as sig
from multiprocessing import freeze_support

if __name__ == '__main__':
	freeze_support()

	sig.sigProfilerExtractor("matrix", "Mutational_Signatures/BRCA/TSS/test", 
		"Mutational_Profiles/BRCA/TSS/6kb/SBS/BRCA_TSS_6kb.SBS96.all", 
		reference_genome = "GRCh38", opportunity_genome = "GRCh38", cpu = -1,
		context_type = "96", minimum_signatures = 1, maximum_signatures = 4)