import sys
import numpy as np
import pandas as pd 
import seaborn as  sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

import Config

sys.setrecursionlimit(1000000)

cancer = Config.args.cancer_type

if Config.args.is_active == "True":
		state = "active"
elif Config.args.is_active == "False" :
	state = "inactive"
if Config.args.is_cancer_specific == "False":
	state = "6kb"

def correlations():
	tss_mutated_genes = pd.read_csv("MAF_Analysis/" + cancer + "/Summaries/TSS/" + \
		state + "/" + cancer.lower() + "-tss-" + state + "_geneSummary.txt", 
		index_col = "Hugo_Symbol", sep = "\t")
	tss_mutated_genes["Region"] = "TSS"

	tts_mutated_genes = pd.read_csv("MAF_Analysis/" + cancer + "/Summaries/TTS/" + \
		state + "/" + cancer.lower() + "-tts-" + state + "_geneSummary.txt",
		index_col = "Hugo_Symbol", sep = "\t")
	tts_mutated_genes["Region"] = "TTS"

	tss_tts_mutated_genes = pd.read_csv("MAF_Analysis/" + cancer + \
		"/Summaries/Genes-Mutated-TSS-TTS/" + state + "/TSS-TTS-" + state + ".tsv",
		index_col = "Hugo_Symbol", sep = "\t")

	genes =  pd.read_csv(Config.args.non_overlapping_genes, index_col = "Name", 
		sep = "\t")
	genes_to_analyze = pd.concat([tss_mutated_genes, tts_mutated_genes])
	genes_to_analyze = genes_to_analyze.join(genes["ID"])
	genes_to_analyze = genes_to_analyze[genes_to_analyze["Region"].notna()]
	genes_to_analyze = genes_to_analyze[genes_to_analyze["ID"].notna()]
	genes_to_analyze = genes_to_analyze.set_index("ID")

	tss_tts_mutated_genes = tss_tts_mutated_genes.join(genes["ID"])
	tss_tts_mutated_genes = tss_tts_mutated_genes[tss_tts_mutated_genes["ID"].notna()]
	tss_tts_mutated_genes = tss_tts_mutated_genes.set_index("ID")

	counts = pd.read_csv("Data/" + cancer + "/Transcriptomics/" + cancer.lower() + \
		"_normalized.tsv", index_col = 0, sep = "\t")

	counts_to_analyze = counts.join(genes_to_analyze["Region"], how = "left")
	tss_counts = counts_to_analyze[counts_to_analyze["Region"] == "TSS"]
	tss_counts.pop("Region")
	tts_counts = counts_to_analyze[counts_to_analyze["Region"] == "TTS"]
	tts_counts.pop("Region")
	tss_tts_counts = counts_to_analyze.loc[list(tss_tts_mutated_genes.index)]
	tss_tts_counts.pop("Region")

	tss_log2 = pd.DataFrame(np.log2(tss_counts + 1))
	tts_log2 = pd.DataFrame(np.log2(tts_counts + 1))
	tss_tts_log2 = pd.DataFrame(np.log2(tss_tts_counts + 1))

	tss_counts_log2 = tss_log2.T.corr()
	tts_counts_log2 = tts_log2.T.corr()
	tss_tts_counts_log2 = tss_tts_log2.T.corr()

	tss_counts_log2.to_csv("Data/" + cancer + "/Correlations/TSS/" + state + \
		"/tss_cor.tsv", sep = "\t", float_format='%.3f')

	tts_counts_log2.to_csv("Data/" + cancer + "/Correlations/TTS/" + state + \
		"/tts_cor.tsv", sep = "\t", float_format='%.3f')

	tss_tts_counts_log2.to_csv("Data/" + cancer + "/Correlations/TSS-TTS/" + \
		state + "/tss_tts_cor.tsv", sep = "\t", float_format='%.3f')

	return(tss_log2, tss_counts_log2, tts_log2, 
		tts_counts_log2, tss_tts_log2, tss_tts_counts)

def clustermap(matrix, region, name, v_min, v_max):
	g = sns.clustermap(matrix, 
	    vmin = v_min, vmax = v_max, 
	    cmap = sns.color_palette("vlag", as_cmap = True), 
	    metric = "euclidean",
	    xticklabels = False, yticklabels = False,
	    method = "ward", figsize = [25, 25])

	g.savefig("Expression_Profiles/" + cancer + "/" + region + "/" + state + \
		"/" + name + ".png", dpi = 300)
	plt.close('all')

if __name__ == '__main__':
	tss_log2, tss_cor, tts_log2, tts_cor, tss_tts_log2, tss_tts_cor = correlations()
	regions = ["TSS", "TTS", "TSS-TTS"]

	for m, r in zip([tss_cor, tts_cor, tss_tts_cor], regions):
		clustermap(m, r, "Co-expression-map", -1, 1)

	for m, r in zip([tss_log2, tts_log2, tss_tts_log2], regions):
		clustermap(m, r, "expression-profile", 
			min(m.min(axis = 1)), max(m.max(axis = 1)))