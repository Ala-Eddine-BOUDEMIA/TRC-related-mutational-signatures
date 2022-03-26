import os
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

matrices = matGen.SigProfilerMatrixGeneratorFunc(
	"BRCA_remain", "GRCh38", "Data/BRCA/Remain/", plot=True)