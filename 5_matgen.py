from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

import Config

cancer = Config.args.cancer_type
region = Config.args.region

matrices = matGen.SigProfilerMatrixGeneratorFunc(
	cancer + "_" + region + "_6kb", "GRCh38", "Data/" + cancer + "/" + region + "/6kb/", plot=True)