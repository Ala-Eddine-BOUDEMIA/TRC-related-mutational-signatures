import pandas as pd 

import Config

coding_genes = pd.read_csv(Config.args.all_coding_genes, 
	index_col="ID", sep="\t")

active_genes = pd.read_csv(Config.args.all_active_genes, 
	index_col="0", sep="\t")

inactive_genes = pd.read_csv(Config.args.all_inactive_genes, 
	index_col="0", sep="\t")

active_coding_genes = active_genes.join(coding_genes, how="inner").drop("Unnamed: 0", axis=1)
inactive_coding_genes = inactive_genes.join(coding_genes, how="inner").drop("Unnamed: 0", axis=1)

active_coding_genes.to_csv(Config.args.active_coding_genes, sep="\t")
inactive_coding_genes.to_csv(Config.args.inactive_coding_genes, sep="\t")