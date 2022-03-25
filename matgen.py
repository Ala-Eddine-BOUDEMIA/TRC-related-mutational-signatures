import os
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

matrices = matGen.SigProfilerMatrixGeneratorFunc(
	"BRCA_No_UTR", "GRCh38", "Data/BRCA/No_UTR/", plot=True)