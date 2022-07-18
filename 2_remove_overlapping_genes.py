import pandas as pd 

import Config
import Tools

pd.set_option('display.max_rows', None)

def remove_overlaps(protein_coding_genes, non_overlapping_genes,
	non_overlapping_genes_plus, non_overlapping_genes_minus):
	
	Tools.create_folder("/".join(str(non_overlapping_genes).split("/")[:-1]))

	genes = pd.read_csv(protein_coding_genes, header=0, sep="\t")
	if Config.args.strand == False:
		genes = genes.sort_values(["Chr", "Start", "End"]).reset_index(drop=True)
	else:
		genes = genes.sort_values(["Strand", "Chr", "Start", "End"]).reset_index(drop=True)
	genes["Length"] = genes["End"] - genes["Start"]

	i = 0
	while i < len(genes)-1:
		overlap = genes.iloc[i+1]["Start"] - genes.iloc[i]["End"]
		if overlap < 0:
			
			if genes.iloc[i]["Chr"] == genes.iloc[i+1]["Chr"] and \
			genes.iloc[i]["Length"] > genes.iloc[i+1]["Length"]:
				genes = genes.drop(i+1, axis=0).reset_index(drop=True)
				continue
			
			elif genes.iloc[i]["Chr"] == genes.iloc[i+1]["Chr"] and \
			genes.iloc[i]["Length"] < genes.iloc[i+1]["Length"]:
				genes = genes.drop(i, axis=0).reset_index(drop=True)
				continue
		
		i += 1

	genes_plus = genes[genes["Strand"]=="+"].reset_index(drop=True)
	genes_minus = genes[genes["Strand"]=="-"].reset_index(drop=True)

	genes.to_csv(non_overlapping_genes, sep="\t", index=False)
	genes_plus.to_csv(non_overlapping_genes_plus, sep="\t", index=False)
	genes_minus.to_csv(non_overlapping_genes_minus, sep="\t", index=False)

if __name__ == '__main__':
	
	remove_overlaps(
		protein_coding_genes = Config.args.protein_coding_genes,
		non_overlapping_genes = Config.args.non_overlapping_genes,
		non_overlapping_genes_plus = Config.args.non_overlapping_genes_plus,
		non_overlapping_genes_minus = Config.args.non_overlapping_genes_minus) 