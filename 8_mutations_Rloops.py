import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

import Config
import Tools

E2 = "E2-2h"
mcf = "MCF7-2h"

def update_df(df):
	
	df["Size"] = df['End'] - df["Start"]
	df = df[df["Size"] <= 8000]
	df["Middle"] = (df["Start"] + df["End"])//2
	df["Start_C"] = df["Start"] - df["Middle"]
	df["End_C"] = df["End"] - df["Middle"]
	df["Mutation_C"] = df["Mutation"] - df["Middle"]

	return df


def plot(df, titre):

	fig = px.histogram(df["Mutation_C"].values,
	                nbins=80, title = titre)

	Tools.create_folder("PCAWG-MCF7-DRIP-Mutations/" + E2)
	path = "PCAWG-MCF7-DRIP-Mutations/" + E2 + "/" + titre + ".html"
	fig.write_html(path)


def overlay_plot(df1, df2, name1, name2, titre):

	fig = go.Figure()
	fig.add_trace(go.Histogram(x=df1["Mutation_C"].values, xbins=dict(size=100), name=name1))
	fig.add_trace(go.Histogram(x=df2["Mutation_C"].values, xbins=dict(size=100), name=name2))

	fig.update_layout(barmode='overlay')
	fig.update_traces(opacity=0.75)
	path = "PCAWG-MCF7-DRIP-Mutations/" + E2 + "/" + titre + ".html"
	fig.write_html(path)


if __name__ == '__main__':

	maf = pd.read_csv("Data/PCAWG_BRCA/Original/pcawg_brca.maf", header=0, sep="\t")
	maf = maf[maf["Variant_Type"]=="SNP"]

	tss = pd.read_csv(Config.args.tss, sep="\t")
	tss["Start"] = tss["Start"] - 1000
	tss["End"] = tss["End"] + 1000
	tss["Strand"] = tss["Strand"].replace(["-"],-1)
	tss["Strand"] = tss["Strand"].replace(["+"],1)
	tss = tss.drop_duplicates(subset=["Chr", "Start", "End"])

	active_tss = pd.read_csv("Annotations/PCAWG_BRCA/TSS/active_tss.tsv", sep="\t") 
	active_tss["Start"] = active_tss["Start"] - 1000
	active_tss["End"] = active_tss["End"] + 1000
	active_tss["Strand"] = active_tss["Strand"].replace(["-"],-1)
	active_tss["Strand"] = active_tss["Strand"].replace(["+"],1)
	active_tss = active_tss.drop_duplicates(subset=["Chr", "Start", "End"])
	
	inactive_tss = pd.read_csv("Annotations/PCAWG_BRCA/TSS/inactive_tss.tsv", sep="\t") 
	inactive_tss["Start"] = inactive_tss["Start"] - 1000
	inactive_tss["End"] = inactive_tss["End"] + 1000
	inactive_tss["Strand"] = inactive_tss["Strand"].replace(["-"],-1)
	inactive_tss["Strand"] = inactive_tss["Strand"].replace(["+"],1)
	inactive_tss = inactive_tss.drop_duplicates(subset=["Chr", "Start", "End"])

	tts = pd.read_csv(Config.args.tts, sep="\t")
	tts["Start"] = tts["Start"] - 1000
	tts["End"] = tts["End"] + 1000
	tts["Strand"] = tts["Strand"].replace(["-"],-1)
	tts["Strand"] = tts["Strand"].replace(["+"],1)
	tts = tts.drop_duplicates(subset=["Chr", "Start", "End"])

	active_tts = pd.read_csv("Annotations/PCAWG_BRCA/TTS/active_tts.tsv", sep="\t") 
	active_tts["Start"] = active_tts["Start"] - 1000
	active_tts["End"] = active_tts["End"] + 1000
	active_tts["Strand"] = active_tts["Strand"].replace(["-"],-1)
	active_tts["Strand"] = active_tts["Strand"].replace(["+"],1)
	active_tts = active_tts.drop_duplicates(subset=["Chr", "Start", "End"])
	
	inactive_tts = pd.read_csv("Annotations/PCAWG_BRCA/TTS/inactive_tts.tsv", sep="\t") 
	inactive_tts["Start"] = inactive_tts["Start"] - 1000
	inactive_tts["End"] = inactive_tts["End"] + 1000
	inactive_tts["Strand"] = inactive_tts["Strand"].replace(["-"],-1)
	inactive_tts["Strand"] = inactive_tts["Strand"].replace(["+"],1)
	inactive_tts = inactive_tts.drop_duplicates(subset=["Chr", "Start", "End"])

	drip = pd.read_csv("Data/PCAWG_MCF7/BED_Files/" + mcf + ".bed", sep="\t")
	drip["Length"] = drip["End"] - drip["Start"]
	drip = drip.sort_values(["Chr", "Start"])
	
	tss_ranges = Tools.extract_ranges_stranded(tss)
	active_tss_ranges = Tools.extract_ranges_stranded(active_tss)
	inactive_tss_ranges = Tools.extract_ranges_stranded(inactive_tss)
	
	tts_ranges = Tools.extract_ranges_stranded(tts) 
	active_tts_ranges = Tools.extract_ranges_stranded(active_tts)
	inactive_tts_ranges = Tools.extract_ranges_stranded(inactive_tts)
	
	drip_ranges = Tools.extract_ranges(drip)
	drip_ranges = Tools.remove_overlaps(drip_ranges)

	tss_mutations, active_tss_mutations, inactive_tss_mutations = [], [], []
	tss_only_mutations, active_tss_only_mutations, inactive_tss_only_mutations = [], [], []
	
	tts_mutations, active_tts_mutations, inactive_tts_mutations = [], [], []
	tts_only_mutations, active_tts_only_mutations, inactive_tts_only_mutations = [], [], []

	drip_mutations = []
	drip_tss_mutations, drip_active_tss, drip_inactive_tss = [], [], []
	drip_tts_mutations, drip_active_tts, drip_inactive_tts = [], [], []
	
	for k in drip_ranges.keys():
		for i in maf[maf["Chromosome"] == k].index:
			m = maf.loc[i, "Start_Position"]
			
			b_drip = None
			guess_loop = 0 
			
			b_tss, b_tss_a, b_tss_i = None, None, None
			guess_tss, guess_tss_a, guess_tss_i = 0, 0, 0
			
			b_tts, b_tts_a, b_tts_i = None, None, None
			guess_tts, guess_tts_a, guess_tts_i = 0, 0, 0

			b_drip, guess_loop = Tools.binary_search(drip_ranges, m, k)
			if b_drip == True:
				drip_mutations.append([k, guess_loop[0], guess_loop[1], m, i])

			b_tss, guess_tss = Tools.binary_search(tss_ranges, m, k)
			if b_tss == True:
				tss_mutations.append([k, guess_tss[0], guess_tss[1], guess_tss[2], m, i])
	
			b_tss_a, guess_tss_a = Tools.binary_search(active_tss_ranges, m, k)
			if b_tss_a == True:
				active_tss_mutations.append([k, guess_tss_a[0], guess_tss_a[1], guess_tss_a[2], m, i])

			b_tss_i, guess_tss_i = Tools.binary_search(inactive_tss_ranges, m, k)
			if b_tss_i == True:
				inactive_tss_mutations.append([k, guess_tss_i[0], guess_tss_i[1], guess_tss_i[2], m, i])

			b_tts, guess_tts = Tools.binary_search(tts_ranges, m, k)
			if b_tts == True:
				tts_mutations.append([k, guess_tts[0], guess_tts[1], guess_tts[2], m, i])

			b_tts_a, guess_tts_a = Tools.binary_search(active_tts_ranges, m, k)
			if b_tts_a == True:
				active_tts_mutations.append([k, guess_tts_a[0], guess_tts_a[1], guess_tts_a[2], m, i])

			b_tts_i, guess_tts_i = Tools.binary_search(inactive_tts_ranges, m, k)
			if b_tts_i == True:
				inactive_tts_mutations.append([k, guess_tts_i[0], guess_tts_i[1], guess_tts_i[2], m, i])

			if b_drip == True:
				if b_tss == True and b_tts == False:
					drip_tss_mutations.append([k, guess_loop[0], guess_loop[1], m, i])

					if b_tss_i == False and b_tss_a == True:
						drip_active_tss.append([k, guess_loop[0], guess_loop[1], m, i])
					elif b_tss_i == True and b_tss_a == False:
						drip_inactive_tss.append([k, guess_loop[0], guess_loop[1], m, i])

				if b_tss == False and b_tts == True:
					drip_tts_mutations.append([k, guess_loop[0], guess_loop[1], m, i])

					if b_tts_i == False and b_tts_a == True:
						drip_active_tts.append([k, guess_loop[0], guess_loop[1], m, i])
					elif b_tts_i == True and b_tts_a == False:
						drip_inactive_tts.append([k, guess_loop[0], guess_loop[1], m, i])

			if b_drip == False: 
				if b_tss == True and b_tts == False:
					tss_only_mutations.append([k, guess_tss[0], guess_tss[1], guess_tss[2], m, i])

					if b_tss_i == False and b_tss_a == True:
						active_tss_only_mutations.append([k, guess_tss_a[0], guess_tss_a[1], guess_tss_a[2], m, i])
					elif b_tss_i == True and b_tss_a == False:
						inactive_tss_only_mutations.append([k, guess_tss_i[0], guess_tss_i[1], guess_tss_i[2], m, i])

				if b_tss == False and b_tts == True:
					tts_only_mutations.append([k, guess_tts[0], guess_tts[1], guess_tts[2], m, i])
				
					if b_tts_i == False and b_tts_a == True:
						active_tts_only_mutations.append([k, guess_tts_a[0], guess_tts_a[1], guess_tts_a[2], m, i])
					elif b_tts_i == True and b_tts_a == False:
						inactive_tts_only_mutations.append([k, guess_tts_i[0], guess_tts_i[1], guess_tts_i[2], m, i])

	c_drip = ["Chr", "Start", "End", "Mutation", "Index"]
	
	drip_mutations_df = pd.DataFrame(drip_mutations, columns=c_drip)
	
	drip_tss_mutations_df = pd.DataFrame(drip_tss_mutations, columns=c_drip)
	drip_active_tss_df = pd.DataFrame(drip_active_tss, columns=c_drip)
	drip_inactive_tss_df = pd.DataFrame(drip_inactive_tss, columns=c_drip)
	
	drip_tts_mutations_df = pd.DataFrame(drip_tts_mutations, columns=c_drip)
	drip_active_tts_df = pd.DataFrame(drip_active_tts, columns=c_drip)
	drip_inactive_tts_df = pd.DataFrame(drip_inactive_tts, columns=c_drip)

	drip_mutations_df = drip_mutations_df.set_index("Index")
	
	drip_tss_mutations_df = drip_tss_mutations_df.set_index("Index")
	drip_active_tss_df = drip_active_tss_df.set_index("Index")
	drip_inactive_tss_df = drip_inactive_tss_df.set_index("Index")
	
	drip_tts_mutations_df = drip_tts_mutations_df.set_index("Index")
	drip_active_tts_df = drip_active_tts_df.set_index("Index")
	drip_inactive_tts_df = drip_inactive_tts_df.set_index("Index")

	c = ["Chr", "Start", "End", "Strand", "Mutation", "Index"]
	
	tss_mutations_df = pd.DataFrame(tss_mutations, columns=c)
	active_tss_mutations_df = pd.DataFrame(active_tss_mutations, columns=c)
	inactive_tss_mutations_df = pd.DataFrame(inactive_tss_mutations, columns=c)
	
	tss_only_mutations_df = pd.DataFrame(tss_only_mutations, columns=c)
	active_tss_only_mutations_df = pd.DataFrame(active_tss_only_mutations, columns=c)
	inactive_tss_only_mutations_df = pd.DataFrame(inactive_tss_only_mutations, columns=c)
	
	tts_mutations_df = pd.DataFrame(tts_mutations, columns=c)
	active_tts_mutations_df = pd.DataFrame(active_tts_mutations, columns=c)
	inactive_tts_mutations_df = pd.DataFrame(inactive_tts_mutations, columns=c)
	
	tts_only_mutations_df = pd.DataFrame(tts_only_mutations, columns=c)
	active_tts_only_mutations_df = pd.DataFrame(active_tts_only_mutations, columns=c)
	inactive_tts_only_mutations_df = pd.DataFrame(inactive_tts_only_mutations, columns=c)
	
	tss_mutations_df = tss_mutations_df.set_index("Index")
	active_tss_mutations_df = active_tss_mutations_df.set_index("Index")
	inactive_tss_mutations_df = inactive_tss_mutations_df.set_index("Index")
	
	tss_only_mutations_df = tss_only_mutations_df.set_index("Index")
	active_tss_only_mutations_df = active_tss_only_mutations_df.set_index("Index")
	inactive_tss_only_mutations_df = inactive_tss_only_mutations_df.set_index("Index")
	
	tts_mutations_df = tts_mutations_df.set_index("Index")
	active_tts_mutations_df = active_tts_mutations_df.set_index("Index")
	inactive_tts_mutations_df = inactive_tts_mutations_df.set_index("Index")
	
	tts_only_mutations_df = tts_only_mutations_df.set_index("Index")
	active_tts_only_mutations_df = active_tts_only_mutations_df.set_index("Index")
	inactive_tts_only_mutations_df = inactive_tts_only_mutations_df.set_index("Index")

	"""
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

	tss_only_mutations_df = tss_mutations_df.drop(tss_drip_mutations_df.index, axis=0)
	tts_only_mutations_df = tts_mutations_df.drop(tts_drip_mutations_df.index, axis=0)
	active_tss_only_mutations_df = active_tss_mutations_df.drop(active_tss_drip_mutations_df.index, axis=0)
	inactive_tss_only_mutations_df = inactive_tss_mutations_df.drop(inactive_tss_drip_mutations_df.index, axis=0)
	active_tts_only_mutations_df = active_tts_mutations_df.drop(active_tts_drip_mutations_df.index, axis=0)
	inactive_tts_only_mutations_df = inactive_tts_mutations_df.drop(inactive_tts_drip_mutations_df.index, axis=0)
	"""

	drip_mutations_df = update_df(drip_mutations_df)
	
	drip_tss_mutations_df = update_df(drip_tss_mutations_df)
	drip_active_tss_df = update_df(drip_active_tss_df)
	drip_inactive_tss_df = update_df(drip_inactive_tss_df)
	
	drip_tts_mutations_df = update_df(drip_tts_mutations_df)
	drip_active_tts_df = update_df(drip_active_tts_df)
	drip_inactive_tts_df = update_df(drip_inactive_tts_df)

	tss_mutations_df = update_df(tss_mutations_df)
	active_tss_mutations_df = update_df(active_tss_mutations_df)
	inactive_tss_mutations_df = update_df(inactive_tss_mutations_df)
	
	tss_only_mutations_df = update_df(tss_only_mutations_df)
	active_tss_only_mutations_df = update_df(active_tss_only_mutations_df)
	inactive_tss_only_mutations_df = update_df(inactive_tss_only_mutations_df)

	tts_mutations_df = update_df(tts_mutations_df)
	active_tts_mutations_df = update_df(active_tts_mutations_df)
	inactive_tts_mutations_df = update_df(inactive_tts_mutations_df)
	
	tts_only_mutations_df = update_df(tts_only_mutations_df)
	active_tts_only_mutations_df = update_df(active_tts_only_mutations_df)
	inactive_tts_only_mutations_df = update_df(inactive_tts_only_mutations_df)

	tss_mutations_df["Mutation_C"] = tss_mutations_df["Mutation_C"] * tss_mutations_df["Strand"]	
	active_tss_mutations_df["Mutation_C"] = active_tss_mutations_df["Mutation_C"] * active_tss_mutations_df["Strand"]
	inactive_tss_mutations_df["Mutation_C"] = inactive_tss_mutations_df["Mutation_C"] * inactive_tss_mutations_df["Strand"]	
	
	tss_only_mutations_df["Mutation_C"] = tss_only_mutations_df["Mutation_C"] * tss_only_mutations_df["Strand"]
	active_tss_only_mutations_df["Mutation_C"] = active_tss_only_mutations_df["Mutation_C"] * active_tss_only_mutations_df["Strand"]
	inactive_tss_only_mutations_df["Mutation_C"] = inactive_tss_only_mutations_df["Mutation_C"] * inactive_tss_only_mutations_df["Strand"]

	tts_mutations_df["Mutation_C"] = tts_mutations_df["Mutation_C"] * tts_mutations_df["Strand"]
	active_tts_mutations_df["Mutation_C"] = active_tts_mutations_df["Mutation_C"] * active_tts_mutations_df["Strand"]
	active_tts_only_mutations_df["Mutation_C"] = active_tts_only_mutations_df["Mutation_C"] * active_tts_only_mutations_df["Strand"]
	
	tts_only_mutations_df["Mutation_C"] = tts_only_mutations_df["Mutation_C"] * tts_only_mutations_df["Strand"]
	inactive_tts_mutations_df["Mutation_C"] = inactive_tts_mutations_df["Mutation_C"] * inactive_tts_mutations_df["Strand"]
	inactive_tts_only_mutations_df["Mutation_C"] = inactive_tts_only_mutations_df["Mutation_C"] * inactive_tts_only_mutations_df["Strand"]

	"""
	tss_mutations_df = tss_mutations_df.merge(
		tss, on = ["Chr", "Start", "End"], how="left").set_index(tss_mutations_df.index)
	tss_mutations_df["Mutation_C"] = tss_mutations_df["Mutation_C"] * tss_mutations_df["Strand"]
	
	tts_mutations_df = tts_mutations_df.merge(
		tts, on = ["Chr", "Start", "End"], how="left").set_index(tts_mutations_df.index)
	tts_mutations_df["Mutation_C"] = tts_mutations_df["Mutation_C"] * tts_mutations_df["Strand"]

	tss_only_mutations_df = tss_only_mutations_df.merge(
		tss, on = ["Chr", "Start", "End"], how="left").set_index(tss_only_mutations_df.index)
	tss_only_mutations_df["Mutation_C"] = tss_only_mutations_df["Mutation_C"] * tss_only_mutations_df["Strand"]
	
	tts_only_mutations_df = tts_only_mutations_df.merge(
		tts, on = ["Chr", "Start", "End"], how="left").set_index(tts_only_mutations_df.index)
	tts_only_mutations_df["Mutation_C"] = tts_only_mutations_df["Mutation_C"] * tts_only_mutations_df["Strand"]

	active_tss_mutations_df = active_tss_mutations_df.merge(
		active_tss, on = ["Chr", "Start", "End"], how="left").set_index(active_tss_mutations_df.index)
	active_tss_mutations_df["Mutation_C"] = active_tss_mutations_df["Mutation_C"] * active_tss_mutations_df["Strand"]
	
	active_tts_mutations_df = active_tts_mutations_df.merge(
		active_tts, on = ["Chr", "Start", "End"], how="left").set_index(active_tts_mutations_df.index)
	active_tts_mutations_df["Mutation_C"] = active_tts_mutations_df["Mutation_C"] * active_tts_mutations_df["Strand"]

	inactive_tss_mutations_df = inactive_tss_mutations_df.merge(
		inactive_tss, on = ["Chr", "Start", "End"], how="left").set_index(inactive_tss_mutations_df.index)
	inactive_tss_mutations_df["Mutation_C"] = inactive_tss_mutations_df["Mutation_C"] * inactive_tss_mutations_df["Strand"]
	
	inactive_tts_mutations_df = inactive_tts_mutations_df.merge(
		inactive_tts, on = ["Chr", "Start", "End"], how="left").set_index(inactive_tts_mutations_df.index)
	inactive_tts_mutations_df["Mutation_C"] = inactive_tts_mutations_df["Mutation_C"] * inactive_tts_mutations_df["Strand"]

	active_tss_only_mutations_df = active_tss_only_mutations_df.merge(
		active_tss, on = ["Chr", "Start", "End"], how="left").set_index(active_tss_only_mutations_df.index)
	active_tss_only_mutations_df["Mutation_C"] = active_tss_only_mutations_df["Mutation_C"] * active_tss_only_mutations_df["Strand"]
	
	active_tts_only_mutations_df = active_tts_only_mutations_df.merge(
		active_tts, on = ["Chr", "Start", "End"], how="left").set_index(active_tts_only_mutations_df.index)
	active_tts_only_mutations_df["Mutation_C"] = active_tts_only_mutations_df["Mutation_C"] * active_tts_only_mutations_df["Strand"]

	inactive_tss_only_mutations_df = inactive_tss_only_mutations_df.merge(
		inactive_tss, on = ["Chr", "Start", "End"], how="left").set_index(inactive_tss_only_mutations_df.index)
	inactive_tss_only_mutations_df["Mutation_C"] = inactive_tss_only_mutations_df["Mutation_C"] * inactive_tss_only_mutations_df["Strand"]
	
	inactive_tts_only_mutations_df = inactive_tts_only_mutations_df.merge(
		inactive_tts, on = ["Chr", "Start", "End"], how="left").set_index(inactive_tts_only_mutations_df.index)
	inactive_tts_only_mutations_df["Mutation_C"] = inactive_tts_only_mutations_df["Mutation_C"] * inactive_tts_only_mutations_df["Strand"]
	"""

	plot(drip_mutations_df, "Mutations_Co-occurring_with_R-Loops")
	
	plot(drip_tss_mutations_df, "Mutations_Co-occurring_with_R-Loops_close_to_TSS")
	plot(drip_active_tss_df, "Mutations_Co-occuring_R-Loops_at_active_TSS_regions")
	plot(drip_inactive_tss_df, "Mutations_Co-occuring_R-Loops_at_inactive_TSS_regions")
	
	plot(drip_tts_mutations_df, "Mutations_Co-occurring_with_R-Loops_close_to_TTS")
	plot(drip_active_tts_df, "Mutations_Co-occuring_R-Loops_at_active_TTS_regions")
	plot(drip_inactive_tts_df, "Mutations_Co-occuring_R-Loops_at_inactive_TTS_regions")

	plot(tss_mutations_df, "Mutations_occurring_at_TSS_regions")
	plot(active_tss_mutations_df, "Mutations_occuring_at_active_TSS_regions")
	plot(inactive_tss_mutations_df, "Mutations_occuring_at_inactive_TSS_regions")
	
	plot(tss_only_mutations_df, "Mutations_occurring_only_at_TSS_regions")
	plot(active_tss_only_mutations_df, "Mutations_occuring_only_at_active_TSS_regions")
	plot(inactive_tss_only_mutations_df, "Mutations_occuring_only_at_inactive_TSS_regions")
	
	plot(tts_mutations_df, "Mutations_occurring_at_TTS_regions")
	plot(active_tts_mutations_df, "Mutations_occuring_at_active_TTS_regions")
	plot(inactive_tts_mutations_df, "Mutations_occuring_at_inactive_TTS_regions")
	
	plot(tts_only_mutations_df, "Mutations_occurring_only_at_TTS_regions")
	plot(active_tts_only_mutations_df, "Mutations_occuring_only_at_active_TTS_regions")
	plot(inactive_tts_only_mutations_df, "Mutations_occuring_only_at_inactive_TTS_regions")

	overlay_plot(drip_active_tss_df, drip_inactive_tss_df,
		"TSS-active-Rloops", "TSS-inactive-Rloops", 
		"Mutations_occurring_at_active_inactive_TSS_Rloops")
	overlay_plot(drip_active_tts_df, drip_inactive_tts_df,
		"TTS-active-Rloops", "TTS-inactive-Rloops", 
		"Mutations_occurring_at_active_inactive_TTS_Rloops")
	overlay_plot(drip_active_tts_df, drip_active_tss_df,
		"TTS-active-Rloops", "TSS-active-Rloops", 
		"Mutations_occurring_at_active_TSS_TTS_Rloops")
	overlay_plot(drip_inactive_tts_df, drip_inactive_tss_df,
		"TTS-inactive-Rloops", "TSS-inactive-Rloops", 
		"Mutations_occurring_at_inactive_TSS_TTS_Rloops")
	
	overlay_plot(active_tss_mutations_df, inactive_tss_mutations_df,
		"TSS-active", "TSS-inactive", 
		"Mutations_occurring_at_active_inactive_TSS")
	overlay_plot(active_tts_mutations_df, inactive_tts_mutations_df,
		"TTS-active", "TTS-inactive", 
		"Mutations_occurring_at_active_inactive_TTS")
	overlay_plot(active_tts_mutations_df, active_tss_mutations_df,
		"TTS-active", "TSS-active", 
		"Mutations_occurring_at_active_TSS_TTS")
	overlay_plot(inactive_tts_mutations_df, inactive_tss_mutations_df,
		"TTS-inactive", "TSS-inactive", 
		"Mutations_occurring_at_inactive_TSS_TTS")

	overlay_plot(active_tss_only_mutations_df, inactive_tss_only_mutations_df,
		"TSS-active-only", "TSS-inactive-only", 
		"Mutations_occurring_at_active_inactive_TSS_only")
	overlay_plot(active_tts_only_mutations_df, inactive_tts_only_mutations_df,
		"TTS-active-only", "TTS-inactive-only", 
		"Mutations_occurring_at_active_inactive_TTS_only")
	overlay_plot(active_tts_only_mutations_df, active_tss_only_mutations_df,
		"TTS-active-only", "TSS-active-only", 
		"Mutations_occurring_at_active_TSS_TTS_only")
	overlay_plot(inactive_tts_only_mutations_df, inactive_tss_only_mutations_df,
		"TTS-inactive-only", "TSS-inactive-only", 
		"Mutations_occurring_at_inactive_TSS_TTS_only")

	overlay_plot(active_tss_only_mutations_df, drip_active_tss_df,
		"TSS-active-only", "TSS-active-Rloops", 
		"Mutations_occurring_at_active_TSS_and_Rloops_TSS")
	overlay_plot(active_tts_only_mutations_df, drip_active_tts_df,
		"TTS-active-only", "TTS-active-Rloops", 
		"Mutations_occurring_at_active_TTS_and_Rloops_TTS")
	overlay_plot(inactive_tss_only_mutations_df, drip_inactive_tss_df,
		"TSS-inactive-only", "TSS-inactive-Rloops", 
		"Mutations_occurring_at_inactive_TSS_and_Rloops_TSS")
	overlay_plot(inactive_tts_only_mutations_df, drip_inactive_tts_df,
		"TTS-inactive-only", "TTS-inactive-Rloops", 
		"Mutations_occurring_at_inactive_TTS_and_Rloops_TTS")

	overlay_plot(drip_tts_mutations_df, drip_tss_mutations_df, 
		"TTS-Rloops", "TSS-Rloops", 
		"Mutations_Co-occurring_with_R-Loops_close_to_TSS_TTS")
	overlay_plot(tts_mutations_df, tss_mutations_df, 
		"TTS-only", "TSS-only", 
		"Mutations_occurring_close_to_TSS_TTS")
	overlay_plot(tts_only_mutations_df, tss_only_mutations_df, 
		"TTS", "TSS", 
		"Mutations_occurring_only_at_TSS_TTS")
	overlay_plot(tss_only_mutations_df, drip_tss_mutations_df, 
		"TSS-only", "TSS-Rloops", 
		"Mutations_occurring_only_at_TSS_or_co-occurring_with_TSS_Rloops")
	overlay_plot(tts_only_mutations_df, drip_tts_mutations_df, 
		"TTS-only", "TTS-Rloops", 
		"Mutations_occurring_only_at_TTS_or_co-occurring_with_TTS_Rloops")

	not_drip = tss_only_mutations_df["Mutation_C"].to_list() + tts_only_mutations_df["Mutation_C"].to_list()
	not_drip_df = pd.DataFrame(not_drip, columns=["Mutation_C"])
	overlay_plot(not_drip_df, drip_mutations_df,
		"Not-Rloops", "Rloops", 
		"Mutations_co-occurring_with_Rloops_and_outside_Rloops")

	drip_mutations_maf = maf.loc[drip_mutations_df.index]
	
	drip_tss_mutations_maf = maf.loc[drip_tss_mutations_df.index]
	drip_tts_mutations_maf = maf.loc[drip_tts_mutations_df.index]
	
	tss_only_mutations_maf = maf.loc[tss_only_mutations_df.index]
	tts_only_mutations_maf = maf.loc[tts_only_mutations_df.index]

	Tools.create_folder("Annotations/PCAWG_MCF7/All/" + E2)
	Tools.create_folder("Annotations/PCAWG_MCF7/TSS/" + E2)
	Tools.create_folder("Annotations/PCAWG_MCF7/TTS/" + E2)
	
	drip_mutations_df.to_csv("Annotations/PCAWG_MCF7/All/" + E2 + "/drip_mutations.tsv", sep="\t", index=False)
	
	drip_tss_mutations_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/drip_mutations.tsv", sep="\t", index=False)
	drip_active_tss_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/active_tss_drip_mutations.tsv", sep="\t", index=False)
	drip_inactive_tss_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/inactive_tss_drip_mutations.tsv", sep="\t", index=False)
	
	drip_tts_mutations_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/drip_mutations.tsv", sep="\t", index=False)
	drip_active_tts_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/active_tts_drip_mutations.tsv", sep="\t", index=False)
	drip_inactive_tts_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/inactive_tts_drip_mutations.tsv", sep="\t", index=False)

	tss_mutations_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/all_tss_mutations.tsv", sep="\t", index=False)
	active_tss_mutations_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/active_tss_mutations.tsv", sep="\t", index=False)
	inactive_tss_mutations_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/inactive_tss_mutations.tsv", sep="\t", index=False)
	
	tss_only_mutations_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/only_tss_mutations.tsv", sep="\t", index=False)
	active_tss_only_mutations_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/active_tss_only_mutations.tsv", sep="\t", index=False)
	inactive_tss_only_mutations_df.to_csv("Annotations/PCAWG_MCF7/TSS/" + E2 + "/inactive_tss_only_mutations.tsv", sep="\t", index=False)
	
	tts_mutations_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/all_tts_mutations.tsv", sep="\t", index=False)
	active_tts_mutations_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/active_tts_mutations.tsv", sep="\t", index=False)
	inactive_tts_mutations_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/inactive_tts_mutations.tsv", sep="\t", index=False)
	
	tts_only_mutations_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/only_tts_mutations.tsv", sep="\t", index=False)
	active_tts_only_mutations_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/active_tts_only_mutations.tsv", sep="\t", index=False)
	inactive_tts_only_mutations_df.to_csv("Annotations/PCAWG_MCF7/TTS/" + E2 + "/inactive_tts_only_mutations.tsv", sep="\t", index=False)

	Tools.create_folder("Data/PCAWG_MCF7/All/" + E2)
	Tools.create_folder("Data/PCAWG_MCF7/TSS/" + E2)
	Tools.create_folder("Data/PCAWG_MCF7/TTS/" + E2)
	
	drip_mutations_maf.to_csv("Data/PCAWG_MCF7/All/" + E2 + "/drip_mutations.maf", sep="\t", index=False)
	
	drip_tss_mutations_maf.to_csv("Data/PCAWG_MCF7/TSS/" + E2 + "/drip_mutations.maf", sep="\t", index=False)
	drip_tts_mutations_maf.to_csv("Data/PCAWG_MCF7/TTS/" + E2 + "/drip_mutations.maf", sep="\t", index=False)
	
	tss_only_mutations_maf.to_csv("Data/PCAWG_MCF7/TSS/" + E2 + "/only_tss_mutations.maf", sep="\t", index=False)
	tts_only_mutations_maf.to_csv("Data/PCAWG_MCF7/TTS/" + E2 + "/only_tts_mutations.maf", sep="\t", index=False)