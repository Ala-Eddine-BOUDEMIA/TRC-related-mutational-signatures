import pandas as pd 
from itertools import islice

chromes = list(map(str,range(1,23)))+['X','Y']
val = 3000
tss, tts = [], []
with open("Annotations/grch38.gtf", "r") as g:
	for line in islice(g, 5, None):
		l = line.split("\t")
		chrom = l[0]
		feature = l[2]
		if chrom in chromes and feature == "transcript":
			strand = l[6]
			gene_id = l[8].split(";")[0].split('"')[1]
			gene_name = l[8].split(";")[4].split('"')[1]
			gene_biotype = l[8].split(";")[6].split('"')[1]
			transcript_id = l[8].split(";")[2].split('"')[1]
			transcript_start = int(l[3])
			transcript_end = int(l[4])
			transcript_length = transcript_end - transcript_start
			if gene_biotype == "protein_coding":
				if strand == "+":
					tss_start = transcript_start - val
					tss_end = transcript_start + val
					tts_start = transcript_end - val
					tts_end = transcript_end + val
				elif strand == "-":
					tss_start = transcript_end - val
					tss_end = transcript_end + val
					tts_start = transcript_start - val
					tts_end = transcript_start + val
				tss.append(["chr"+chrom, tss_start, tss_end, strand, 
					gene_id, gene_name, transcript_id, transcript_length])
				tts.append(["chr"+chrom, tts_start, tts_end, strand, 
					gene_id, gene_name, transcript_id, transcript_length])

tss_df = pd.DataFrame(tss, 
	columns = ["Chr", "Start", "End", 
	"Strand", "Gene_ID", "Gene_Name",
	"Transcript_ID", "Transcript_Length"])
tss_df = tss_df.loc[tss_df.groupby('Gene_Name')['Transcript_Length'].idxmax()]
tss_df = tss_df.sort_values(["Chr", "Start"])
tss_df.to_csv("Annotations/tss_gtf.tsv", sep="\t", index=False)

tts_df = pd.DataFrame(tts, 
	columns = ["Chr", "Start", "End", 
	"Strand", "Gene_ID", "Gene_Name",
	"Transcript_ID", "Transcript_Length"])
tts_df = tts_df.loc[tts_df.groupby('Gene_Name')['Transcript_Length'].idxmax()]
tts_df = tts_df.sort_values(["Chr", "Start"])
tts_df.to_csv("Annotations/tts_gtf.tsv", sep="\t", index=False)