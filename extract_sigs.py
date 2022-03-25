from SigProfilerExtractor import sigpro as sig

sig.sigProfilerExtractor("matrix", "Mutational_Signatures/BRCA/Keep/3UTR", 
	"Mutational_Profiles/BRCA/Keep/3UTR/SBS/BRCA_3UTR_Keep.SBS96.all", 
	reference_genome = "GRCh38", opportunity_genome = "GRCh38",
	context_type = "96", minimum_signatures = 1, maximum_signatures = 4)