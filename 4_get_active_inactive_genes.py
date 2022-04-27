import pandas as pd 

import Config


def get_genes_by_type(cancer, active_genes_path, inactive_genes_path):
	
	coding_genes = pd.read_csv(Config.args.non_overlapping_genes, 
		index_col="ID", sep="\t")

	active_genes = pd.read_csv("Annotations/" + cancer + "/all_active_genes.tsv", 
		index_col="0", sep="\t")

	inactive_genes = pd.read_csv("Annotations/" + cancer + "/all_inactive_genes.tsv", 
		index_col="0", sep="\t")

	active_coding_genes = active_genes.join(coding_genes, how="inner")
	inactive_coding_genes = inactive_genes.join(coding_genes, how="inner")

	print("Number of active genes: ", len(active_coding_genes))
	print("Number of inactive genes: ", len(inactive_coding_genes))

	active_coding_genes.to_csv(active_genes_path, sep="\t", index=False)
	inactive_coding_genes.to_csv(inactive_genes_path, sep="\t", index=False)

if __name__ == '__main__':
	
	get_genes_by_type(
		cancer = Config.args.cancer_type,
		active_genes_path = Config.args.active_genes,
		inactive_genes_path = Config.args.inactive_genes)