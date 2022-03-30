import pandas as pd 
from itertools import islice

chromes = list(map(str,range(1,23)))+['X','Y']
val = 3000
tss, tts = [], []
with open("Annotations/coding_genes.bed","r") as f:
	for line in islice(f, 1, None):
		l = line.split("\t")
		if l[-1].strip() == "+":
			tss_start = int(l[1]) - val
			tss_end = int(l[1]) + val
			tts_start = int(l[2]) - val
			tts_end = int(l[2]) + val
		else:
			tss_start = int(l[2]) - val
			tss_end = int(l[2]) + val
			tts_start = int(l[1]) - val
			tts_end = int(l[1]) + val

		tss.append([l[0], tss_start, tss_end, l[3], l[-1].strip()])
		tts.append([l[0], tts_start, tts_end, l[3], l[-1].strip()])

tss_df = pd.DataFrame(tss, 
	columns = ["Chr", "Start", "End", "Gene_Name", "Strand"]).sort_values(["Chr","Start"])
tss_df.to_csv("Annotations/tss_y.tsv", sep="\t", index=False)

tts_df = pd.DataFrame(tts, 
	columns = ["Chr", "Start", "End", "Gene_Name", "Strand"]).sort_values(["Chr","Start"])
tts_df.to_csv("Annotations/tts_y.tsv", sep="\t", index=False)