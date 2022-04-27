import pandas as pd 

import Config

cancer = Config.args.cancer_type

coding_genes = pd.read_csv(Config.args.non_overlapping_genes, 
	index_col="ID", sep="\t")

active_genes = pd.read_csv("Annotations/" + cancer + "/all_genes/all_active_genes.tsv", 
	index_col="0", sep="\t")

inactive_genes = pd.read_csv("Annotations/" + cancer + "/all_genes/all_inactive_genes.tsv", 
	index_col="0", sep="\t")

active_coding_genes = active_genes.join(coding_genes, how="inner")
inactive_coding_genes = inactive_genes.join(coding_genes, how="inner")

print("Number of active genes: ", len(active_coding_genes))
print("Number of inactive genes: ", len(inactive_coding_genes))

active_coding_genes.to_csv("Annotations/" + cancer + "/coding_genes/active_coding_genes.tsv", sep="\t")
inactive_coding_genes.to_csv("Annotations/" + cancer + "/coding_genes/inactive_coding_genes.tsv", sep="\t")