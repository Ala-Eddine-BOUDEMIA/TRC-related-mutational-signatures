import pandas as pd 

import Config

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

def binary_search(ranges, item, k, i):
	
	low = 0
	high = len(ranges[k]) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = ranges[k][mid]
		if item in range(guess[0], guess[1]+1):
			return True
		elif guess[0] > item:
			high = mid - 1
		else:
			low = mid + 1
	return False

def sort_indeces(ranges, maf):

	index = []
	for i in maf.index:
		if binary_search(ranges, maf.at[i,"Start_Position"], 
		maf.at[i,"Chromosome"], i) == True:
			index.append(i)
	return index

if __name__ == '__main__':
	
	dataset = Config.args.dataset
	maf = pd.read_csv("Data/" + dataset + "/Original/" + \
		dataset.lower() + ".maf", header = 5, sep = "\t")
	maf = maf[maf["Variant_Type"]=="SNP"]

	conv = pd.read_csv(Config.args.conv, sep = "\t")
	r_conv = extract_ranges(conv)
	index_conv = sort_indeces(r_conv, maf)
	print("Number of mutations between convergent genes: ", len(index_conv))
	maf_conv = maf.loc[index_conv]
	maf_conv.to_csv("Data/" + dataset + "/Convergent/conv.maf", sep="\t", index=False)
	
	div = pd.read_csv(Config.args.div, sep = "\t")
	r_div = extract_ranges(div)
	index_div = sort_indeces(r_div, maf)
	print("Number of mutations between divergent genes: ", len(index_div))
	maf_div = maf.loc[index_div]
	maf_div.to_csv("Data/" + dataset + "/Divergent/div.maf", sep="\t", index=False)
	
	tand = pd.read_csv(Config.args.tand, sep = "\t")
	r_tand = extract_ranges(tand)
	index_tand = sort_indeces(r_tand, maf)
	print("Number of mutations between tandent genes: ", len(index_tand))
	maf_tand = maf.loc[index_tand]
	maf_tand.to_csv("Data/" + dataset + "/Tandem/co.maf", sep="\t", index=False)