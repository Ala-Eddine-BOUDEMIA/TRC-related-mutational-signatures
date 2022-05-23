import pandas as pd 

import Config
import Binary_search
import Ranges_extractor

pd.set_option('display.max_rows', None)

def sort_indeces(ranges, maf):
	
	index = []
	for i in maf.index:
		strand = "+" if maf.at[i,"TRANSCRIPT_STRAND"] == +1 else "-"
		if Binary_search.binary_search_stranded(ranges, maf.at[i,"Start_Position"], 
		strand, maf.at[i,"Chromosome"]) == True:
			index.append(i)
	return index

if __name__ == '__main__':
	
	dataset = Config.args.dataset
	state = Config.args.state

	if state == "active":
		tss_paths = [Config.args.active_tss]
		tts_paths = [Config.args.active_tts]
	if state == "inactive":
		tss_paths = [Config.args.inactive_tss]
		tts_paths = [Config.args.inactive_tts]
	if state == "6kb":
		tss_path = [Config.args.tss]
		tts_path = [Config.args.tts]

	maf = pd.read_csv("Data/" + dataset + "/Original/" + \
		dataset.lower() + ".maf", header=5, sep="\t")
	maf = maf[maf["Variant_Type"]=="SNP"]

	for tss_path, tts_path in zip(tss_paths, tts_paths):
	
		tss = pd.read_csv(tss_path, header=0, sep="\t")
		tts = pd.read_csv(tts_path, header=0, sep="\t")

		l_tss = Ranges_extractor.extract_ranges_stranded(tss)
		l_tts = Ranges_extractor.extract_ranges_stranded(tts)

		index_tss = sort_indeces(l_tss, maf)
		print("Number of mutations on TSS: ", len(index_tss))
		index_tts = sort_indeces(l_tts, maf)
		print("Number of mutations on TTS: ", len(index_tts))

		maf_tss = maf.loc[index_tss]
		maf_tts = maf.loc[index_tts]
		
		intersection = maf_tss.index.intersection(maf_tts.index)
		print("Number of mutations in common: ", len(intersection))
		print("These mutations will be discarded")

		maf_tss = maf_tss.drop(pd.Series(intersection), axis=0)
		maf_tts = maf_tts.drop(pd.Series(intersection), axis=0)

		maf_tss.to_csv("Data/" + dataset + "/TSS/" + state + "/tss.maf", 
			sep="\t", index=False)
		maf_tts.to_csv("Data/" + dataset + "/TTS/" + state + "/tts.maf", 
			sep="\t", index=False)
			
		index = list(set(index_tss + index_tts))
		maf_not_utr = maf.drop(pd.Series(index), axis=0)
		maf_not_utr.to_csv("Data/" + dataset + "/Remain/" + state + "/remain.maf", 
			sep="\t", index=False)