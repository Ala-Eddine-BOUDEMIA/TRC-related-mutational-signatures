from SigProfilerExtractor import sigpro as sig

sig.sigProfilerExtractor("matrix", "Mutational_Signatures/BRCA/TSS/6kb", 
	"Mutational_Profiles/BRCA/TSS/6kb/SBS/BRCA_TSS_6kb.SBS96.all", 
	reference_genome = "GRCh38", opportunity_genome = "GRCh38",
	context_type = "96", minimum_signatures = 1, maximum_signatures = 4)