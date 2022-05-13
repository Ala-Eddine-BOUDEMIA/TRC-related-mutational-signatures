import pandas as pd 

import Config

pd.set_option('display.max_rows', None)

def extract_ranges(df):
	
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

def remove_overlaps(ranges):
	
	for s in ranges.keys():	
		for k in ranges[s].keys():
			i = 0
			while i < len(ranges[s][k]) - 1:
				if min(ranges[s][k][i][1], ranges[s][k][i + 1][1]) \
				>= max(ranges[s][k][i][0], ranges[s][k][i + 1][0]):
					ranges[s][k][i] = [
						min(ranges[s][k][i][0], ranges[s][k][i + 1][0]), 
						max(ranges[s][k][i][1], ranges[s][k][i + 1][1])]
					ranges[s][k].pop(i + 1)
				else:
					i += 1
	return ranges

def binary_search(ranges, item, s, k):
	
	low = 0
	high = len(ranges[s][k]) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = ranges[s][k][mid]
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
		strand = "+" if maf.at[i,"TRANSCRIPT_STRAND"] == +1 else "-"
		if binary_search(ranges, maf.at[i,"Start_Position"], 
		strand, maf.at[i,"Chromosome"]) == True:
			index.append(i)
	return index

if __name__ == '__main__':
	
	dataset = Config.args.dataset
	if Config.args.is_active == True:
		state = "active"
		tss_paths = [Config.args.active_tss]
		tts_paths = [Config.args.active_tts]
	elif Config.args.is_active == False :
		state = "inactive"
		tss_paths = [Config.args.inactive_tss]
		tts_paths = [Config.args.inactive_tts]

	if Config.args.is_global == True:
		state = "6kb"
		tss_path = [Config.args.tss]
		tts_path = [Config.args.tts]

	maf = pd.read_csv("Data/" + dataset + "/Original/" + \
		dataset.lower() + ".maf", header=5, sep="\t")
	maf = maf[maf["Variant_Type"]=="SNP"]

	for tss_path, tts_path in zip(tss_paths, tts_paths):
	
		tss = pd.read_csv(tss_path, header=0, sep="\t")
		tts = pd.read_csv(tts_path, header=0, sep="\t")

		l_tss = extract_ranges(tss)
		l_tts = extract_ranges(tts)

		#l_tss = remove_overlaps(l_tss)
		#l_tts = remove_overlaps(l_tts)

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