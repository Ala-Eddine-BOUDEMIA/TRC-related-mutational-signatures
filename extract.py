from SigProfilerExtractor import sigpro as sig

sig.sigProfilerExtractor("matrix", "Mutational_Signatures/BLCA/results", 
	"Mutational_Profiles/BLCA/output/SBS/BLCA.SBS96.all", 
	reference_genome = "GRCh38", opportunity_genome = "GRCh38",
	context_type = "96", minimum_signatures = 1, maximum_signatures = 7)