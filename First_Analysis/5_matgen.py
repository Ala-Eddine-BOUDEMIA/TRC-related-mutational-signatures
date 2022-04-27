from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

import Config

cancer = Config.args.cancer_type
region = Config.args.region

if Config.args.cluster:
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		cancer + "_" + region + "_6kb", "GRCh38", "/local/scratch/mutational_profiles/Data/" + cancer + "/" + region + "/6kb/", plot=True)
else:
	matrices = matGen.SigProfilerMatrixGeneratorFunc(
		cancer + "_" + region + "_6kb", "GRCh38", "Data/" + cancer + "/" + region + "/6kb/", plot=True)

