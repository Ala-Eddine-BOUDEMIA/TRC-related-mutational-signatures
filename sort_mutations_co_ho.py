import pandas as pd 

import Config
import Binary_search
import Ranges_extractor

def sort_indeces(ranges, maf):

	index = []
	for i in maf.index:
		b, _ = Binary_search.binary_search(
			ranges, maf.at[i,"Start_Position"], maf.at[i,"Chromosome"], i) 

		if b == True:
			index.append(i)
			
	return index

if __name__ == '__main__':
	
	dataset = Config.args.dataset
	maf = pd.read_csv("Data/" + dataset + "/Original/" + \
		dataset.lower() + ".maf", header = 5, sep = "\t")
	maf = maf[maf["Variant_Type"]=="SNP"]

	conv = pd.read_csv(Config.args.conv, sep = "\t")
	r_conv = Ranges_extractor.extract_ranges(conv)
	index_conv = sort_indeces(r_conv, maf)
	print("Number of mutations between convergent genes: ", len(index_conv))
	maf_conv = maf.loc[index_conv]
	maf_conv.to_csv("Data/" + dataset + "/Convergent/conv.maf", sep="\t", index=False)
	
	div = pd.read_csv(Config.args.div, sep = "\t")
	r_div = Ranges_extractor.extract_ranges(div)
	index_div = sort_indeces(r_div, maf)
	print("Number of mutations between divergent genes: ", len(index_div))
	maf_div = maf.loc[index_div]
	maf_div.to_csv("Data/" + dataset + "/Divergent/div.maf", sep="\t", index=False)
	
	tand = pd.read_csv(Config.args.tand, sep = "\t")
	r_tand = Ranges_extractor.extract_ranges(tand)
	index_tand = sort_indeces(r_tand, maf)
	print("Number of mutations between tandent genes: ", len(index_tand))
	maf_tand = maf.loc[index_tand]
	maf_tand.to_csv("Data/" + dataset + "/Tandem/co.maf", sep="\t", index=False)