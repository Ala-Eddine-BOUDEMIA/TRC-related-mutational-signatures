import pandas as pd 
from itertools import islice

chromes = list(map(str,range(1,23)))+['X','Y']
val = 3000
tss, tts = [], []
with open("Annotations/coding_genes_hg38_NOV_0kb.bed","r") as f:
	for line in islice(f, 1, None):
		l = line.split("\t")
		if l[5].strip() == "+":
			tss_start = int(l[1]) - val
			tss_end = int(l[1]) + val
			tts_start = int(l[2]) - val
			tts_end = int(l[2]) + val
		else:
			tss_start = int(l[2]) - val
			tss_end = int(l[2]) + val
			tts_start = int(l[1]) - val
			tts_end = int(l[1]) + val

		tss.append([l[0], tss_start, tss_end, l[3], l[4], l[5].strip()])
		tts.append([l[0], tts_start, tts_end, l[3], l[4], l[5].strip()])

tss_df = pd.DataFrame(tss, 
	columns = ["Chr", "Start", "End", "Name", "Score", "Strand"]).sort_values(["Chr","Start"])
tss_df.to_csv("Annotations/tss.tsv", sep="\t", index=False)

tts_df = pd.DataFrame(tts, 
	columns = ["Chr", "Start", "End", "Name", "Score", "Strand"]).sort_values(["Chr","Start"])
tts_df.to_csv("Annotations/tts.tsv", sep="\t", index=False)