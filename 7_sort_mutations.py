import pandas as pd 

import Config
import Tools

pd.set_option('display.max_rows', None)

def sort_indeces(ranges, maf):
	
	index = []
	for i in maf.index:
		b, _ = Tools.binary_search(ranges, 
			maf.at[i,"Start_Position"], maf.at[i,"Chromosome"])
		
		if b == True:
			index.append(i)
	
	return index

if __name__ == '__main__':
	
	dataset = Config.args.dataset
	state = Config.args.state
	region_type = Config.args.region

	if region_type != "TSS-TTS" or region_type != "CO-HO":
		print("Warning: Region type is not adapted for this script")
		print("Please change the parameter in Config or via command line --region")

	maf = pd.read_csv("Data/" + dataset + "/Original/" + \
		dataset.lower() + ".maf", header=5, sep="\t")
	maf = maf[maf["Variant_Type"]=="SNP"]

	if region_type == "TSS-TTS":
		if state == "active":
			tss_paths = [Config.args.active_tss]
			tts_paths = [Config.args.active_tts]
		if state == "inactive":
			tss_paths = [Config.args.inactive_tss]
			tts_paths = [Config.args.inactive_tts]
		if state == "6kb":
			tss_paths = [Config.args.tss]
			tts_paths = [Config.args.tts]

		for tss_path, tts_path in zip(tss_paths, tts_paths):
		
			tss = pd.read_csv(tss_path, header=0, sep="\t")
			tts = pd.read_csv(tts_path, header=0, sep="\t")

			l_tss = Tools.extract_ranges(tss)
			l_tts = Tools.extract_ranges(tts)
			
			l_tss = Tools.remove_overlaps(l_tss)
			l_tts = Tools.remove_overlaps(l_tts)

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

			Tools.create_folder("Data/" + dataset + "/TSS/" + state)
			Tools.create_folder("Data/" + dataset + "/TTS/" + state)
			Tools.create_folder("Data/" + dataset + "/Remain/" + state)
			
			maf_tss.to_csv("Data/" + dataset + "/TSS/" + state + "/tss.maf", 
				sep="\t", index=False)
			maf_tts.to_csv("Data/" + dataset + "/TTS/" + state + "/tts.maf", 
				sep="\t", index=False)
				
			index = list(set(index_tss + index_tts))
			maf_not_utr = maf.drop(pd.Series(index), axis=0)
			maf_not_utr.to_csv("Data/" + dataset + "/Remain/" + state + "/remain.maf", 
				sep="\t", index=False)

	elif region_type == "CO-HO":
		
		conv = pd.read_csv(Config.args.conv, sep = "\t")
		r_conv = Ranges_extractor.extract_ranges(conv)
		index_conv = sort_indeces(r_conv, maf)
		print("Number of mutations between convergent genes: ", len(index_conv))
		maf_conv = maf.loc[index_conv]
		Tools.create_folder("Data/" + dataset + "/Convergent/")
		maf_conv.to_csv("Data/" + dataset + "/Convergent/conv.maf", sep="\t", index=False)
		
		div = pd.read_csv(Config.args.div, sep = "\t")
		r_div = Ranges_extractor.extract_ranges(div)
		index_div = sort_indeces(r_div, maf)
		print("Number of mutations between divergent genes: ", len(index_div))
		maf_div = maf.loc[index_div]
		Tools.create_folder("Data/" + dataset + "/Divergent/")
		maf_div.to_csv("Data/" + dataset + "/Divergent/div.maf", sep="\t", index=False)
		
		tand = pd.read_csv(Config.args.tand, sep = "\t")
		r_tand = Ranges_extractor.extract_ranges(tand)
		index_tand = sort_indeces(r_tand, maf)
		print("Number of mutations between tandent genes: ", len(index_tand))
		maf_tand = maf.loc[index_tand]
		Tools.create_folder("Data/" + dataset + "/Tandem/")
		maf_tand.to_csv("Data/" + dataset + "/Tandem/co.maf", sep="\t", index=False)