import pandas as pd 
import plotly.express as px

import Config
import Binary_search
import Ranges_extractor

drip = pd.read_csv("Data/MCF7-DRIP/identified_DRIP_peaks_mock.bed", sep="\t")
tss = pd.read_csv(Config.args.tss, sep="\t")
tts = pd.read_csv(Config.args.tts, sep="\t")
maf = pd.read_csv("Data/BRCA/Original/brca.maf", header=5, sep="\t")
maf = maf[maf["Variant_Type"]=="SNP"]

drip["Length"] = drip["End"] - drip["Start"]
fig = px.histogram(drip, x="Length", title="R-Loops Length Distribution")
#fig.show()

drip_ranges = Ranges_extractor.extract_ranges(drip)
tss_ranges = Ranges_extractor.extract_ranges(tss)
tts_ranges = Ranges_extractor.extract_ranges(tts) 

for k in drip_ranges.keys():
	for i in maf[maf["Chromosome"]==k].index:
		b, ind = Binary_search.binary_search(drip_ranges, maf.at[i, "Start_Position"], k) 
		if b == True:
			drip_ranges[k][ind][2] +=1

drip_tss =  []
for k in tss_ranges.keys():
	for i in drip_ranges[k]:
		for j in tss_ranges[k]:
			if min(i[1], j[1]) >= max(i[0], j[0]):
				drip_tss.append([k, i[0], i[1], i[2]])

drip_tts =  []
for k in tts_ranges.keys():
	for i in drip_ranges[k]:
		for j in tts_ranges[k]:
			if min(i[1], j[1]) >= max(i[0], j[0]):
				drip_tts.append([k, i[0], i[1], i[2]])

drip_tss_df = pd.DataFrame(drip_tss, columns=[["Chr", "Start", "End", "Mutations"]])
drip_tts_df = pd.DataFrame(drip_tts, columns=[["Chr", "Start", "End", "Mutations"]])

drip_tss_df.to_csv("Annotations/MCF7/TSS/drip_tss_mck.tsv", sep="\t", index=False)
drip_tts_df.to_csv("Annotations/MCF7/TTS/drip_tts_mck.tsv", sep="\t", index=False)