import pandas as pd

def extract_ranges(df):
	
	ranges = {"chr1":[], "chr2":[], "chr3":[], "chr4":[], "chr5":[], "chr6":[], 
		"chr7":[], "chr8":[], "chr9":[], "chr10":[], "chr11":[], "chr12":[], 
		"chr13":[], "chr14":[], "chr15":[], "chr16":[], "chr17":[], "chr18":[], 
		"chr19":[], "chr20":[], "chr21":[], "chr22":[], "chrX":[], "chrY":[]}

	for i in df.index:
		chr_ = df.at[i, "Chr"]

		if chr_ in ranges.keys():
			start_pos = df.at[i, "Start"]
			end_pos = df.at[i, "End"]
			ranges[chr_].append([start_pos, end_pos])

	for k in ranges.keys():
		ranges[k].sort(key=lambda x:x[-1])

	return ranges

def extract_ranges_stranded(df):
	
	ranges = {
		"+":{"chr1":[], "chr2":[], "chr3":[], "chr4":[], "chr5":[], "chr6":[], 
		"chr7":[], "chr8":[], "chr9":[], "chr10":[], "chr11":[], "chr12":[], 
		"chr13":[], "chr14":[], "chr15":[], "chr16":[], "chr17":[], "chr18":[], 
		"chr19":[], "chr20":[], "chr21":[], "chr22":[], "chrX":[], "chrY":[]},
	
		"-":{"chr1":[], "chr2":[], "chr3":[], "chr4":[], "chr5":[], "chr6":[], 
		"chr7":[], "chr8":[], "chr9":[], "chr10":[], "chr11":[], "chr12":[], 
		"chr13":[], "chr14":[], "chr15":[], "chr16":[], "chr17":[], "chr18":[], 
		"chr19":[], "chr20":[], "chr21":[], "chr22":[], "chrX":[], "chrY":[]}
		}

	for i in df.index:
		chr_ = df.at[i, "Chr"]
		strand = df.at[i, "Strand"]
	
		if chr_ in ranges[strand].keys():
			start_pos = df.at[i, "Start"]
			end_pos = df.at[i, "End"]
			ranges[strand][chr_].append([start_pos, end_pos])

	for s in ranges.keys():
		for k in ranges[s].keys():
			ranges[s][k].sort(key=lambda x:x[-1])
	
	return ranges