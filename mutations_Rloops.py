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
	path = "MCF7-DRIP-Mutations/E2-24h/" + titre + ".html"
	fig.write_html(path)

def overlay_plot(df1, df2, bins1, bins2, name1, name2, titre):

	fig = go.Figure()
	fig.add_trace(go.Histogram(x=df1["Mutations_C"].values, nbinsx=bins1, name=name1))
	fig.add_trace(go.Histogram(x=df2["Mutations_C"].values, nbinsx=bins2, name=name2))

	fig.update_layout(barmode='overlay')
	fig.update_traces(opacity=0.75)
	path = "MCF7-DRIP-Mutations/E2-24h/" + titre + ".html"
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

	active_brca_tss = pd.read_csv("Annotations/BRCA/TSS/active_tss.tsv", sep="\t") 
	active_brca_tss["Start"] = active_brca_tss["Start"] - 1000
	active_brca_tss["End"] = active_brca_tss["End"] + 1000
	
	inactive_brca_tss = pd.read_csv("Annotations/BRCA/TSS/inactive_tss.tsv", sep="\t") 
	inactive_brca_tss["Start"] = inactive_brca_tss["Start"] - 1000
	inactive_brca_tss["End"] = inactive_brca_tss["End"] + 1000

	active_brca_tts = pd.read_csv("Annotations/BRCA/TTS/active_tts.tsv", sep="\t") 
	active_brca_tts["Start"] = active_brca_tts["Start"] - 1000
	active_brca_tts["End"] = active_brca_tts["End"] + 1000
	
	inactive_brca_tts = pd.read_csv("Annotations/BRCA/TTS/inactive_tts.tsv", sep="\t") 
	inactive_brca_tts["Start"] = inactive_brca_tts["Start"] - 1000
	inactive_brca_tts["End"] = inactive_brca_tts["End"] + 1000

	drip = pd.read_csv("Data/MCF7/BED_Files/mcf7-24h.bed", sep="\t")
	drip["Length"] = drip["End"] - drip["Start"]
	drip = drip.sort_values(["Chr", "Start"])

	tss_ranges = Ranges_extractor.extract_ranges(tss)
	tts_ranges = Ranges_extractor.extract_ranges(tts) 
	active_tss_ranges = Ranges_extractor.extract_ranges(active_brca_tss)
	inactive_tss_ranges = Ranges_extractor.extract_ranges(inactive_brca_tss)
	active_tts_ranges = Ranges_extractor.extract_ranges(active_brca_tts)
	inactive_tts_ranges = Ranges_extractor.extract_ranges(inactive_brca_tts)
	drip_ranges = Ranges_extractor.extract_ranges(drip)
	drip_ranges = Remove_overlaps.remove_overlaps(drip_ranges)

	drip_mutations = []
	tss_mutations = []
	tts_mutations = []
	active_tss_mutations = []
	inactive_tss_mutations = []
	active_tts_mutations = []
	inactive_tts_mutations = []

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

	for k in active_tss_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:
			m = maf.loc[i, "Start_Position"]
			b, guess = Binary_search.binary_search(active_tss_ranges, m, k)
			if b == True:
				active_tss_mutations.append([k, guess[0], guess[1], m, i])

	for k in inactive_tss_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:
			m = maf.loc[i, "Start_Position"]
			b, guess = Binary_search.binary_search(inactive_tss_ranges, m, k)
			if b == True:
				inactive_tss_mutations.append([k, guess[0], guess[1], m, i])

	for k in active_tts_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:
			m = maf.loc[i, "Start_Position"]
			b, guess = Binary_search.binary_search(active_tts_ranges, m, k)
			if b == True:
				active_tts_mutations.append([k, guess[0], guess[1], m, i])

	for k in inactive_tts_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:
			m = maf.loc[i, "Start_Position"]
			b, guess = Binary_search.binary_search(inactive_tts_ranges, m, k)
			if b == True:
				inactive_tts_mutations.append([k, guess[0], guess[1], m, i])

	c = ["Chr", "Start", "End", "Mutation", "Index"]
	drip_mutations_df = pd.DataFrame(drip_mutations, columns=c)
	tss_mutations_df = pd.DataFrame(tss_mutations, columns=c)
	tts_mutations_df = pd.DataFrame(tts_mutations, columns=c)
	active_tss_mutations_df = pd.DataFrame(active_tss_mutations, columns=c)
	inactive_tss_mutations_df = pd.DataFrame(inactive_tss_mutations, columns=c)
	active_tts_mutations_df = pd.DataFrame(active_tts_mutations, columns=c)
	inactive_tts_mutations_df = pd.DataFrame(inactive_tts_mutations, columns=c)

	drip_mutations_df = drip_mutations_df.set_index("Index")
	tss_mutations_df = tss_mutations_df.set_index("Index")
	tts_mutations_df = tts_mutations_df.set_index("Index")
	active_tss_mutations_df = active_tss_mutations_df.set_index("Index")
	inactive_tss_mutations_df = inactive_tss_mutations_df.set_index("Index")
	active_tts_mutations_df = active_tts_mutations_df.set_index("Index")
	inactive_tts_mutations_df = inactive_tts_mutations_df.set_index("Index")

	mutations_tss_drip = drip_mutations_df.index.intersection(tss_mutations_df.index)
	mutations_tts_drip = drip_mutations_df.index.intersection(tts_mutations_df.index)
	mutations_active_tss_drip = drip_mutations_df.index.intersection(active_tss_mutations_df.index)
	mutations_inactive_tss_drip = drip_mutations_df.index.intersection(inactive_tss_mutations_df.index)
	mutations_active_tts_drip = drip_mutations_df.index.intersection(active_tts_mutations_df.index)
	mutations_inactive_tts_drip = drip_mutations_df.index.intersection(inactive_tts_mutations_df.index)

	tss_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_tss_drip)]
	tts_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_tts_drip)]
	active_tss_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_active_tss_drip)]
	inactive_tss_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_inactive_tss_drip)]
	active_tts_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_active_tts_drip)]
	inactive_tts_drip_mutations_df = drip_mutations_df.loc[pd.Series(mutations_inactive_tts_drip)]

	#mutations_tss_only = tss_drip_mutations_df.index.intersection(tss_mutations_df.index)
	#mutations_tts_only = tts_drip_mutations_df.index.intersection(tts_mutations_df.index)
	#mutations_active_tss_only = active_tss_drip_mutations_df.index.intersection(active_tss_mutations_df.index)
	#mutations_inactive_tss_only = inactive_tss_drip_mutations_df.index.intersection(inactive_tss_mutations_df.index)
	#mutations_active_tts_only = active_tts_drip_mutations_df.index.intersection(active_tts_mutations_df.index)
	#mutations_inactive_tts_only = inactive_tts_drip_mutations_df.index.intersection(inactive_tts_mutations_df.index)

	tss_only_mutations_df = tss_mutations_df.drop(tss_drip_mutations_df.index, axis=0)
	tts_only_mutations_df = tts_mutations_df.drop(tts_drip_mutations_df.index, axis=0)
	active_tss_only_mutations_df = active_tss_mutations_df.drop(active_tss_drip_mutations_df.index, axis=0)
	inactive_tss_only_mutations_df = inactive_tss_mutations_df.drop(inactive_tss_drip_mutations_df.index, axis=0)
	active_tts_only_mutations_df = active_tts_mutations_df.drop(active_tts_drip_mutations_df.index, axis=0)
	inactive_tts_only_mutations_df = inactive_tts_mutations_df.drop(inactive_tts_drip_mutations_df.index, axis=0)

	drip_mutations_df = update_df(drip_mutations_df)
	tss_mutations_df = update_df(tss_mutations_df)
	tts_mutations_df = update_df(tts_mutations_df)
	tss_drip_mutations_df = update_df(tss_drip_mutations_df)
	tts_drip_mutations_df = update_df(tts_drip_mutations_df)
	tss_only_mutations_df = update_df(tss_only_mutations_df)
	tts_only_mutations_df = update_df(tts_only_mutations_df)
	active_tss_mutations_df = update_df(active_tss_mutations_df)
	inactive_tss_mutations_df = update_df(inactive_tss_mutations_df)
	active_tts_mutations_df = update_df(active_tts_mutations_df)
	inactive_tts_mutations_df = update_df(inactive_tts_mutations_df)
	active_tss_drip_mutations_df = update_df(active_tss_drip_mutations_df)
	inactive_tss_drip_mutations_df = update_df(inactive_tss_drip_mutations_df)
	active_tts_drip_mutations_df = update_df(active_tts_drip_mutations_df)
	inactive_tts_drip_mutations_df = update_df(inactive_tts_drip_mutations_df)
	active_tss_only_mutations_df = update_df(active_tss_only_mutations_df)
	inactive_tss_only_mutations_df = update_df(inactive_tss_only_mutations_df)
	active_tts_only_mutations_df = update_df(active_tts_only_mutations_df)
	inactive_tts_only_mutations_df = update_df(inactive_tts_only_mutations_df)

	plot(drip_mutations_df, 80, "Mutations_Co-occurring_with_R-Loops")
	plot(tss_mutations_df, 160, "Mutations_occurring_at_TSS_regions")
	plot(tts_mutations_df, 160, "Mutations_occurring_at_TTS_regions")
	plot(tss_drip_mutations_df, 80, "Mutations_Co-occurring_with_R-Loops_close_to_TSS")
	plot(tts_drip_mutations_df, 80, "Mutations_Co-occurring_with_R-Loops_close_to_TTS")
	plot(tss_only_mutations_df, 160, "Mutations_occurring_only_at_TSS_regions")
	plot(tts_only_mutations_df, 160, "Mutations_occurring_only_at_TTS_regions")
	
	plot(active_tss_mutations_df, 160, "Mutations_occuring_at_active_TSS_regions")
	plot(inactive_tss_mutations_df, 160, "Mutations_occuring_at_inactive_TSS_regions")
	plot(active_tts_mutations_df, 160, "Mutations_occuring_at_active_TTS_regions")
	plot(inactive_tts_mutations_df, 160, "Mutations_occuring_at_inactive_TTS_regions")
	
	plot(active_tss_drip_mutations_df, 80, "Mutations_Co-occuring_R-Loops_at_active_TSS_regions")
	plot(inactive_tss_drip_mutations_df, 80, "Mutations_Co-occuring_R-Loops_at_inactive_TSS_regions")
	plot(active_tts_drip_mutations_df, 80, "Mutations_Co-occuring_R-Loops_at_active_TTS_regions")
	plot(inactive_tts_drip_mutations_df, 80, "Mutations_Co-occuring_R-Loops_at_inactive_TTS_regions")
	
	plot(active_tss_only_mutations_df, 160, "Mutations_occuring_only_at_active_TSS_regions")
	plot(inactive_tss_only_mutations_df, 160, "Mutations_occuring_only_at_inactive_TSS_regions")
	plot(active_tts_only_mutations_df, 160, "Mutations_occuring_only_at_active_TTS_regions")
	plot(inactive_tts_only_mutations_df, 160, "Mutations_occuring_only_at_inactive_TTS_regions")

	overlay_plot(active_tss_mutations_df, inactive_tss_mutations_df,
		160, 160, "TSS-active", "TSS-inactive", 
		"Mutations_occurring_at_active_inactive_TSS")
	overlay_plot(active_tts_mutations_df, inactive_tts_mutations_df,
		160, 160, "TTS-active", "TTS-inactive", 
		"Mutations_occurring_at_active_inactive_TTS")
	overlay_plot(active_tts_mutations_df, active_tss_mutations_df,
		160, 160, "TTS-active", "TSS-active", 
		"Mutations_occurring_at_active_TSS_TTS")
	overlay_plot(inactive_tts_mutations_df, inactive_tss_mutations_df,
		160, 160, "TTS-inactive", "TSS-inactive", 
		"Mutations_occurring_at_inactive_TSS_TTS")

	overlay_plot(active_tss_drip_mutations_df, inactive_tss_drip_mutations_df,
		80, 80, "TSS-active-Rloops", "TSS-inactive-Rloops", 
		"Mutations_occurring_at_active_inactive_TSS_Rloops")
	overlay_plot(active_tts_drip_mutations_df, inactive_tts_drip_mutations_df,
		80, 80, "TTS-active-Rloops", "TTS-inactive-Rloops", 
		"Mutations_occurring_at_active_inactive_TTS_Rloops")
	overlay_plot(active_tts_drip_mutations_df, active_tss_drip_mutations_df,
		80, 80, "TTS-active-Rloops", "TSS-active-Rloops", 
		"Mutations_occurring_at_active_TSS_TTS_Rloops")
	overlay_plot(inactive_tts_drip_mutations_df, inactive_tss_drip_mutations_df,
		80, 80, "TTS-inactive-Rloops", "TSS-inactive-Rloops", 
		"Mutations_occurring_at_inactive_TSS_TTS_Rloops")

	overlay_plot(active_tss_only_mutations_df, inactive_tss_only_mutations_df,
		160, 160, "TSS-active-only", "TSS-inactive-only", 
		"Mutations_occurring_at_active_inactive_TSS_only")
	overlay_plot(active_tts_only_mutations_df, inactive_tts_only_mutations_df,
		160, 160, "TTS-active-only", "TTS-inactive-only", 
		"Mutations_occurring_at_active_inactive_TTS_only")
	overlay_plot(active_tts_only_mutations_df, active_tss_only_mutations_df,
		160, 160, "TTS-active-only", "TSS-active-only", 
		"Mutations_occurring_at_active_TSS_TTS_only")
	overlay_plot(inactive_tts_only_mutations_df, inactive_tss_only_mutations_df,
		160, 160, "TTS-inactive-only", "TSS-inactive-only", 
		"Mutations_occurring_at_inactive_TSS_TTS_only")

	overlay_plot(active_tss_only_mutations_df, active_tss_drip_mutations_df,
		160, 80, "TSS-active-only", "TSS-active-Rloops", 
		"Mutations_occurring_at_active_TSS_and_Rloops_TSS")
	overlay_plot(active_tts_only_mutations_df, active_tts_drip_mutations_df,
		160, 80, "TTS-active-only", "TTS-active-Rloops", 
		"Mutations_occurring_at_active_TTS_andRloops_TTS")
	overlay_plot(inactive_tss_only_mutations_df, inactive_tss_drip_mutations_df,
		160, 80, "TSS-inactive-only", "TSS-inactive-Rloops", 
		"Mutations_occurring_at_inactive_TSS_and_Rloops_TSS")
	overlay_plot(inactive_tts_only_mutations_df, inactive_tts_drip_mutations_df,
		160, 80, "TTS-inactive-only", "TTS-inactive-Rloops", 
		"Mutations_occurring_at_inactive_TTS_andRloops_TTS")
	
	overlay_plot(tts_drip_mutations_df, tss_drip_mutations_df, 
		80, 80, "TTS-Rloops", "TSS-Rloops", 
		"Mutations_Co-occurring_with_R-Loops_close_to_TSS_TTS")
	overlay_plot(tts_mutations_df, tss_mutations_df, 
		160, 160, "TTS-only", "TSS-only", 
		"Mutations_occurring_close_to_TSS_TTS")
	overlay_plot(tts_only_mutations_df, tss_only_mutations_df, 
		160, 160, "TTS", "TSS", 
		"Mutations_occurring_only_at_TSS_TTS")
	overlay_plot(tss_only_mutations_df, tss_drip_mutations_df, 
		160, 80, "TSS-only", "TSS-Rloops", 
		"Mutations_occurring_only_at_TSS_or_co-occurring_with_TSS_Rloops")
	overlay_plot(tts_only_mutations_df, tts_drip_mutations_df, 
		160, 80, "TTS-only", "TTS-Rloops", 
		"Mutations_occurring_only_at_TTS_or_co-occurring_with_TTS_Rloops")

	not_drip = tss_only_mutations_df["Mutations_C"].to_list() + tts_only_mutations_df["Mutations_C"].to_list()
	not_drip_df = pd.DataFrame(not_drip, columns=["Mutations_C"])
	overlay_plot(not_drip_df, drip_mutations_df,
		160, 80, "Not-Rloops", "Rloops", 
		"Mutations_co-occurring_with_Rloops_and_outside_Rloops")

	drip_mutations_maf = maf.loc[drip_mutations_df.index]
	tss_drip_mutations_maf = maf.loc[tss_drip_mutations_df.index]
	tts_drip_mutations_maf = maf.loc[tts_drip_mutations_df.index]
	tss_only_mutations_maf = maf.loc[tss_only_mutations_df.index]
	tts_only_mutations_maf = maf.loc[tts_only_mutations_df.index]

	drip_mutations_df.to_csv("Annotations/MCF7/All/E2-24h/drip_mutations.tsv", sep="\t", index=False)
	tss_drip_mutations_df.to_csv("Annotations/MCF7/TSS/E2-24h/drip_mutations.tsv", sep="\t", index=False)
	tts_drip_mutations_df.to_csv("Annotations/MCF7/TTS/E2-24h/drip_mutations.tsv", sep="\t", index=False)
	tss_mutations_df.to_csv("Annotations/MCF7/TSS/E2-24h/all_tss_mutations.tsv", sep="\t", index=False)
	tts_mutations_df.to_csv("Annotations/MCF7/TTS/E2-24h/all_tts_mutations.tsv", sep="\t", index=False)
	tss_only_mutations_df.to_csv("Annotations/MCF7/TSS/E2-24h/only_tss_mutations.tsv", sep="\t", index=False)
	tts_only_mutations_df.to_csv("Annotations/MCF7/TTS/E2-24h/only_tts_mutations.tsv", sep="\t", index=False)

	drip_mutations_maf.to_csv("Data/MCF7/All/E2-24h/drip_mutations.maf", sep="\t", index=False)
	tss_drip_mutations_maf.to_csv("Data/MCF7/TSS/E2-24h/drip_mutations.maf", sep="\t", index=False)
	tts_drip_mutations_maf.to_csv("Data/MCF7/TTS/E2-24h/drip_mutations.maf", sep="\t", index=False)
	tss_only_mutations_maf.to_csv("Data/MCF7/TSS/E2-24h/only_tss_mutations.maf", sep="\t", index=False)
	tts_only_mutations_maf.to_csv("Data/MCF7/TTS/E2-24h/only_tts_mutations.maf", sep="\t", index=False)