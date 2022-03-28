#!usr/bin/python3.8
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

matrices = matGen.SigProfilerMatrixGeneratorFunc("BLCA_TSS", "GRCh38", "Data/BLCA/TSS/", plot=True)