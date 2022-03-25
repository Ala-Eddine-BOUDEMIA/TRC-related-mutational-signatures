import pandas as pd 
from itertools import islice

chromes = list(map(str,range(1,23)))+['X','Y']
val = 300
tss, tts = [], []
with open("Annotations/grch38.gtf", "r") as g:
	for line in islice(g, 5, None):
		l = line.split("\t")
		feature = l[2]
		chrom = l[0]
		if chrom in chromes and feature == "transcript":
			strand = l[6]
			gene_id = l[8].split(";")[0].split('"')[1]
			transcript_id = l[8].split(";")[2].split('"')[1]
			transcript_start = int(l[3])
			transcript_end = int(l[4])
			if strand == "+":
				tss_start = transcript_start - 1 - val
				tss_end = transcript_start + 1 + val
				tts_start = transcript_end - 1 - val
				tts_end = transcript_end + 1 + val
			elif strand == "-":
				tss_start = transcript_end - 1 - val
				tss_end = transcript_end + 1 + val
				tts_start = transcript_start - 1 - val
				tts_end = transcript_start + 1 + val
			tss.append(["chr"+chrom, tss_start, tss_end, strand, gene_id, transcript_id])
			tts.append(["chr"+chrom, tts_start, tts_end, strand, gene_id, transcript_id])

tss_df = pd.DataFrame(tss, 
	columns = ["Chr", "Start", 
	"End", "Strand", "Gene_ID", 
	"Transcript_ID"])
tss_df.to_csv("Annotations/tss.tsv", sep="\t")

tts_df = pd.DataFrame(tts, 
	columns = ["Chr", "Start", 
	"End", "Strand", "Gene_ID", 
	"Transcript_ID"])
tts_df.to_csv("Annotations/tts.tsv", sep="\t")
