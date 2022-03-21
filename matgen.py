from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

matrices = matGen.SigProfilerMatrixGeneratorFunc("BLCA", "GRCh38", 
	"/Users/aboudemi/Documents/Internship/Mutational_Profiles/BLCA/",
	plot=True)