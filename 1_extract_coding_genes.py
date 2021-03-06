import pandas as pd 
from itertools import islice

import Tools
import Config

def extract_genes(genes_path):

	Tools.create_folder("/".join(str(genes_path).split("/")[:-1]))

	chromes = ["chr1", "chr2", "chr3", "chr4", "chr5", 
		"chr6", "chr7", "chr8", "chr9", "chr10", "chr11", 
		"chr12", "chr13", "chr14", "chr15", "chr16", "chr17", 
		"chr18", "chr19", "chr20", "chr21","chr22", "chrX", "chrY"]
	genes = []

	with open(Config.args.gff3, "r") as g:
		for line in islice(g, 0, None):
			try:
				l = line.split("\t")
				chrom = l[0]
				feature = l[2]
				if chrom in chromes and feature == "gene":
					gene_start = int(l[3])
					gene_end = int(l[4])
					gene_name = l[8].split(";")[3].split('=')[1]
					gene_id = l[8].split(";")[1].split('=')[1].split(".")[0]
					gene_type = l[8].split(";")[2].split('=')[1]
					strand = l[6]
					score = 0
					if gene_type == "protein_coding":
						genes.append([chrom, gene_start, gene_end, gene_name, score, strand, gene_id])
			except:	
				pass

	genes_df = pd.DataFrame(genes, columns=["Chr", "Start", "End", "Name", "Score", "Strand", "ID"])
	genes_df.to_csv(genes_path, sep="\t", index=False)

if __name__ == '__main__':
	
	extract_genes(
		genes_path = Config.args.protein_coding_genes)