import pandas as pd 
from itertools import islice

chromes = ["chr1", "chr2", "chr3", "chr4", "chr5", 
	"chr6", "chr7", "chr8", "chr9", "chr10", "chr11", 
	"chr12", "chr13", "chr14", "chr15", "chr16", "chr17", 
	"chr18", "chr19", "chr20", "chr21","chr22", "chrX", "chrY"]
val = 3000
tss, tts = [], []

with open("Annotations/grch38.gff3", "r") as g:
	for line in islice(g, 0, None):
		try:
			l = line.split("\t")
			chrom = l[0]
			feature = l[2]
			if chrom in chromes and feature == "gene":
				gene_start = int(l[3])
				gene_end = int(l[4])
				gene_length = gene_end - gene_start
				strand = l[6]
				gene_id = l[8].split(";")[1].split('=')[1].split(".")[0]
				gene_type = l[8].split(";")[2].split('=')[1]
				gene_name = l[8].split(";")[3].split('=')[1]
				if gene_type == "protein_coding":
					if strand == "+":
						tss_start = gene_start - val
						tss_end = gene_start + val
						tts_start = gene_end - val
						tts_end = gene_end + val
					elif strand == "-":
						tss_start = gene_end - val
						tss_end = gene_end + val
						tts_start = gene_start - val
						tts_end = gene_start + val
					tss.append([chrom, tss_start, tss_end, strand, 
						gene_id, gene_name, gene_length])
					tts.append([chrom, tts_start, tts_end, strand, 
						gene_id, gene_name, gene_length])
		except:
			pass

tss_df = pd.DataFrame(tss, 
	columns = ["Chr", "Start", "End", "Strand", 
	"Gene_ID", "Gene_Name", "Gene_Length"])
tss_df.to_csv("Annotations/tss.tsv", sep="\t", index=False)

tts_df = pd.DataFrame(tts, 
	columns = ["Chr", "Start", "End", "Strand", 
	"Gene_ID", "Gene_Name", "Gene_Length"])
tts_df.to_csv("Annotations/tts.tsv", sep="\t", index=False)
