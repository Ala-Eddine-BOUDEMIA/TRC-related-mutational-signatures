import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

import Config
import Binary_search
import Remove_overlaps
import Ranges_extractor

def update_df(df):
	
	df["Size"] = df['End'] - df["Start"]
	df = df[df["Size"] <= 8000]
	df["Middle"] = (df["Start"] + df["End"])//2
	df["Start_C"] = df["Start"] - df["Middle"]
	df["End_C"] = df["End"] - df["Middle"]
	df["Mutations_C"] = df["Mutation"] - df["Middle"]
	return df

def plot(df, bins, titre):
	
	fig = px.histogram(df["Mutations_C"].values,
	                nbins=bins, title = titre)
	path = "MCF7-DRIP-Mutations/Control/" + titre + ".html"
	fig.write_html(path)

def overlay_plot(df1, df2, bins, titre):
	fig = go.Figure()
	fig.add_trace(go.Histogram(x=df1["Mutations_C"].values, nbinsx=bins, name=titre))
	fig.add_trace(go.Histogram(x=df2["Mutations_C"].values, nbinsx=bins, name=titre))

	fig.update_layout(barmode='overlay')
	fig.update_traces(opacity=0.75)
	path = "MCF7-DRIP-Mutations/Control/" + titre + ".html"
	fig.write_html(path)

if __name__ == '__main__':

	maf = pd.read_csv("Data/BRCA/Original/brca.maf", header=5, sep="\t")
	maf = maf[maf["Variant_Type"]=="SNP"]

	tss = pd.read_csv(Config.args.tss, sep="\t")
	tss["Start"] = tss["Start"] - 1000
	tss["End"] = tss["End"] + 1000
	
	tts = pd.read_csv(Config.args.tts, sep="\t")
	tts["Start"] = tts["Start"] - 1000
	tts["End"] = tts["End"] + 1000

	drip = pd.read_csv("Data/MCF7-DRIP/BED_Files/mcf7-ctrl.bed", sep="\t")
	drip["Length"] = drip["End"] - drip["Start"]
	drip = drip.sort_values(["Chr", "Start"])

	tss_ranges = Ranges_extractor.extract_ranges(tss)
	tts_ranges = Ranges_extractor.extract_ranges(tts) 
	drip_ranges = Ranges_extractor.extract_ranges(drip)
	drip_ranges = Remove_overlaps.remove_overlaps(drip_ranges)

	drip_mutations = []
	tss_mutations = []
	tts_mutations = []

	for k in drip_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:

			m = maf.loc[i, "Start_Position"]
			b, loop = Binary_search.binary_search(drip_ranges, m, k)
			if b == True:
				drip_mutations.append([k, loop[0], loop[1], m, i])

	for k in tss_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:
			m = maf.loc[i, "Start_Position"]
			b, guess = Binary_search.binary_search(tss_ranges, m, k)
			if b == True:
				tss_mutations.append([k, guess[0], guess[1], m, i])

	for k in tts_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:
			m = maf.loc[i, "Start_Position"]
			b, guess = Binary_search.binary_search(tts_ranges, m, k)
			if b == True:
				tts_mutations.append([k, guess[0], guess[1], m, i])

	c = ["Chr", "Start", "End", "Mutation", "Index"]
	drip_mutations_df = pd.DataFrame(drip_mutations, columns=c)
	tss_mutations_df = pd.DataFrame(tss_mutations, columns=c)
	tts_mutations_df = pd.DataFrame(tts_mutations, columns=c)

	drip_mutations_df = drip_mutations_df.set_index("Index")
	tss_mutations_df = tss_mutations_df.set_index("Index")
	tts_mutations_df = tts_mutations_df.set_index("Index")

	mutations_tss_drip = drip_mutations_df.index.intersection(tss_mutations_df.index)
	mutations_tts_drip = drip_mutations_df.index.intersection(tts_mutations_df.index)

	tss_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_tss_drip)]
	tts_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_tts_drip)]

	mutations_tss_only = tss_drip_mutations_df.index.intersection(tss_mutations_df.index)
	mutations_tts_only = tts_drip_mutations_df.index.intersection(tts_mutations_df.index)

	tss_only_mutations_df = tss_mutations_df.drop(pd.Series(mutations_tss_only), axis=0)
	tts_only_mutations_df = tts_mutations_df.drop(pd.Series(mutations_tts_only), axis=0)

	drip_mutations_df = update_df(drip_mutations_df)
	tss_drip_mutations_df = update_df(tss_drip_mutations_df)
	tts_drip_mutations_df = update_df(tts_drip_mutations_df)
	tss_mutations_df = update_df(tss_mutations_df)
	tts_mutations_df = update_df(tts_mutations_df)
	tss_only_mutations_df = update_df(tss_only_mutations_df)
	tts_only_mutations_df = update_df(tts_only_mutations_df)

	plot(drip_mutations_df, 80, "Mutations_Co-occurring_with_R-Loops")
	plot(tss_drip_mutations_df, 80, "Mutations_Co-occurring_with_R-Loops_close_to_TSS")
	plot(tts_drip_mutations_df, 80, "Mutations_Co-occurring_with_R-Loops_close_to_TTS")
	plot(tss_mutations_df, 160, "Mutations_occurring_at_TSS_regions")
	plot(tts_mutations_df, 160, "Mutations_occurring_at_TTS_regions")
	plot(tss_only_mutations_df, 160, "Mutations_occurring_only_at_TSS_regions")
	plot(tts_only_mutations_df, 160, "Mutations_occurring_only_at_TTS_regions")

	overlay_plot(tss_drip_mutations_df, tts_drip_mutations_df, 
		80, "Mutations_Co-occurring_with_R-Loops_close_to_TSS_TTS")
	overlay_plot(tss_mutations_df, tts_mutations_df, 
		80, "Mutations_occurring_close_to_TSS_TTS")
	overlay_plot(tss_only_mutations_df, tts_only_mutations_df, 
		80, "Mutations_occurring_only_at_TSS_TTS")
	overlay_plot(tss_only_mutations_df, tss_drip_mutations_df, 
		80, "Mutations_occurring_only_at_TSS_or_co-occurring_with_TSS_Rloops")
	overlay_plot(tts_only_mutations_df, tts_drip_mutations_df, 
		80, "Mutations_occurring_only_at_TTS_or_co-occurring_with_TTS_Rloops")

	not_drip = tss_only_mutations_df["Mutations_C"].to_list() + tts_only_mutations_df["Mutations_C"].to_list()
	not_drip_df = pd.DataFrame(not_drip, columns=["Mutations_C"])
	overlay_plot(drip_mutations_df, not_drip_df, 
		80, "Mutations_co-occurring_with_Rloops_and_outside_Rloops")

	drip_mutations_maf = maf.loc[drip_mutations_df.index]
	tss_drip_mutations_maf = maf.loc[tss_drip_mutations_df.index]
	tts_drip_mutations_maf = maf.loc[tts_drip_mutations_df.index]
	tss_only_mutations_maf = maf.loc[tss_only_mutations_df.index]
	tts_only_mutations_maf = maf.loc[tts_only_mutations_df.index]

	drip_mutations_df.to_csv("Annotations/MCF7/All/Control/drip_mutations.tsv", sep="\t", index=False)
	tss_drip_mutations_df.to_csv("Annotations/MCF7/TSS/Control/drip_mutations.tsv", sep="\t", index=False)
	tts_drip_mutations_df.to_csv("Annotations/MCF7/TTS/Control/drip_mutations.tsv", sep="\t", index=False)
	tss_mutations_df.to_csv("Annotations/MCF7/TSS/Control/all_tss_mutations.tsv", sep="\t", index=False)
	tts_mutations_df.to_csv("Annotations/MCF7/TTS/Control/all_tts_mutations.tsv", sep="\t", index=False)
	tss_only_mutations_df.to_csv("Annotations/MCF7/TSS/Control/only_tss_mutations.tsv", sep="\t", index=False)
	tts_only_mutations_df.to_csv("Annotations/MCF7/TTS/Control/only_tts_mutations.tsv", sep="\t", index=False)

	drip_mutations_maf.to_csv("Data/MCF7-Drip/All/Control/drip_mutations.maf", sep="\t", index=False)
	tss_drip_mutations_maf.to_csv("Data/MCF7-Drip/TSS/Control/drip_mutations.maf", sep="\t", index=False)
	tts_drip_mutations_maf.to_csv("Data/MCF7-Drip/TTS/Control/drip_mutations.maf", sep="\t", index=False)
	tss_only_mutations_maf.to_csv("Data/MCF7-Drip/TSS/Control/only_tss_mutations.maf", sep="\t", index=False)
	tts_only_mutations_maf.to_csv("Data/MCF7-Drip/TTS/Control/only_tts_mutations.maf", sep="\t", index=False)