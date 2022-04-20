import pandas as pd 

pd.set_option('display.max_rows', None)

genes = pd.read_csv("Annotations/all_coding_genes_hg38.bed", header=0, sep="\t")
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

genes.to_csv("Annotations/coding_genes_hg38_NOV_0kb.bed", sep="\t", index=False)
genes_plus.to_csv("Annotations/coding_genes_plus_hg38_NOV_0kb.bed", sep="\t", index=False)
genes_minus.to_csv("Annotations/coding_genes_minus_hg38_NOV_0kb.bed", sep="\t", index=False)