import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

import Config
import Binary_search
import Remove_overlaps
import Ranges_extractor

drip = pd.read_csv("Data/MCF7-DRIP/mcf7-24h.bed", sep="\t")
tss = pd.read_csv(Config.args.tss, sep="\t")
tts = pd.read_csv(Config.args.tts, sep="\t")
maf = pd.read_csv("Data/BRCA/Original/brca.maf", header=5, sep="\t")
maf = maf[maf["Variant_Type"]=="SNP"]

drip["Length"] = drip["End"] - drip["Start"]
fig = px.histogram(drip, x="Length", title="R-Loops Length Distribution")
fig.write_html("MCF7-DRIP-Mutations/Rloops_length_distribution.html")

drip = drip.sort_values(["Chr", "Start"])

drip_ranges = Ranges_extractor.extract_ranges(drip)
#Merge overlapping loops
drip_nov = Remove_overlaps.remove_overlaps(drip_ranges)
for k in drip_nov.keys():
	for li in drip_nov[k]:
		li.append(0) 

tss_ranges = Ranges_extractor.extract_ranges(tss)
tts_ranges = Ranges_extractor.extract_ranges(tts) 

for k in drip_nov.keys():
	for i in maf[maf["Chromosome"]==k].index:
		b, loop = Binary_search.binary_search(
			drip_nov, maf.at[i, "Start_Position"], k) 
		
		if b == True:
			ind = drip_nov[k].index(loop)
			drip_nov[k][ind][2] += 1
			drip_nov[k][ind].append(maf.at[i, "Start_Position"])

drip_all = []
for k in drip_nov.keys():
	for i in drip_nov[k]:
		drip_all.append([k, i[0], i[1], i[2]] + i[3:])

drip_all_df = pd.DataFrame(drip_all)
drip_all_df["Size"] = drip_all_df[2] - drip_all_df[1]
drip_all_df = drip_all_df[drip_all_df["Size"] <= 8000]
drip_all_df["Middle"] = (drip_all_df[1] + drip_all_df[2])//2
drip_all_df["Start"] = drip_all_df[1] - drip_all_df["Middle"]
drip_all_df["End"] = drip_all_df[2] - drip_all_df["Middle"]
drip_all_df.iloc[:,4:-4] = drip_all_df.iloc[:,4:-4].rsub(drip_all_df["Middle"],0)
drip_all_df.pop("Size") 
drip_all_df.to_csv("Annotations/MCF7/All/drip_mut_24h.tsv", sep="\t", index=False)

mutations = drip_all_df.iloc[:, 4:-3]
li=[]
for i in mutations.columns:
	li = li + mutations.loc[:,i].dropna().to_list()

li_dict = dict.fromkeys(range(-4000,4000,100),0)
for i in li:
	for j in li_dict.keys():
		if i in range(j, j+100):
			li_dict[j] += 1

li_df = pd.DataFrame.from_dict(li_dict, orient="index")
li_df.to_csv('rloops.tsv',sep="\t")
"""
fig = ff.create_distplot([li],['rloops'], show_hist = False)
fig.show()
"""

fig = px.histogram(li, nbins=80)
fig.write_html("MCF7-DRIP-Mutations/mutations_in_rloops.html")

drip_tss = []
for k in drip_nov.keys():
	for i in drip_nov[k]:
		for j in tss_ranges[k]:
			if min(i[1], j[1]) >= max(i[0], j[0]):
				drip_tss.append([k, i[0], i[1], i[2]] + i[3:])
				break

drip_tss_df = pd.DataFrame(drip_tss)
drip_tss_df["Size"] = drip_tss_df[2] - drip_tss_df[1]
drip_tss_df = drip_tss_df[drip_tss_df["Size"] <= 8000]
drip_tss_df["Middle"] = (drip_tss_df[1] + drip_tss_df[2])//2
drip_tss_df["Start"] = drip_tss_df[1] - drip_tss_df["Middle"]
drip_tss_df["End"] = drip_tss_df[2] - drip_tss_df["Middle"]
drip_tss_df.iloc[:,4:-4] = drip_tss_df.iloc[:,4:-4].rsub(drip_tss_df["Middle"],0)
drip_tss_df.pop("Size") 
drip_tss_df.to_csv("Annotations/MCF7/TSS/drip_tss_mut_24h.tsv", sep="\t", index=False)

mutations = drip_tss_df.iloc[:, 4:-3]
li_tss=[]
for i in mutations.columns:
	li_tss = li_tss + mutations.loc[:,i].dropna().to_list()

li_tss_dict = dict.fromkeys(range(-4000,4000,100),0)
for i in li_tss:
	for j in li_tss_dict.keys():
		if i in range(j, j+100):
			li_tss_dict[j] += 1

li_tss_df = pd.DataFrame.from_dict(li_tss_dict, orient="index")
li_tss_df.to_csv('rloops_tss.tsv',sep="\t")

"""
fig = ff.create_distplot([li_tss],['rloops_tss'], show_hist = False)
fig.show()
"""
fig = px.histogram(li_tss, nbins=80, title="TSS")
fig.write_html('MCF7-DRIP-Mutations/tss_rloops_mutations.html')

drip_tts = []
for k in drip_nov.keys():
	for i in drip_nov[k]:
		for j in tts_ranges[k]:
			if min(i[1], j[1]) >= max(i[0], j[0]):
				drip_tts.append([k, i[0], i[1], i[2]] + i[3:])
				break

drip_tts_df = pd.DataFrame(drip_tts)
drip_tts_df["Size"] = drip_tts_df[2] - drip_tts_df[1]
drip_tts_df = drip_tts_df[drip_tts_df["Size"] <= 8000]
drip_tts_df["Middle"] = (drip_tts_df[1] + drip_tts_df[2])//2
drip_tts_df["Start"] = drip_tts_df[1] - drip_tts_df["Middle"]
drip_tts_df["End"] = drip_tts_df[2] - drip_tts_df["Middle"]
drip_tts_df.iloc[:,4:-4] = drip_tts_df.iloc[:,4:-4].rsub(drip_tts_df["Middle"],0)
drip_tts_df.pop("Size") 
drip_tts_df.to_csv("Annotations/MCF7/TTS/drip_tts_mut_24h.tsv", sep="\t", index=False)

mutations = drip_tts_df.iloc[:, 4:-3]
li_tts=[]
for i in mutations.columns:
	li_tts = li_tts + mutations.loc[:,i].dropna().to_list()

li_tts_dict = dict.fromkeys(range(-4000,4000,100),0)
for i in li_tts:
	for j in li_tts_dict.keys():
		if i in range(j, j+100):
			li_tts_dict[j] += 1

li_tts_df = pd.DataFrame.from_dict(li_tts_dict, orient="index")
li_tts_df.to_csv('rloops_tts.tsv',sep="\t")

"""
fig = ff.create_distplot([li_tts],['rloops_tts'], show_hist = False)
fig.show()
"""
fig = px.histogram(li_tts, nbins=80, title="TTS")
fig.write_html('MCF7-DRIP-Mutations/tts_rloops_mutations.html')
"""
fig = ff.create_distplot([li_tss, li_tts],['rloop_tss', 'rloops_tts'], show_hist = False)
fig.show()
"""
fig = go.Figure()
fig.add_trace(go.Histogram(x=li_tts, nbinsx=80, name="TTS"))
fig.add_trace(go.Histogram(x=li_tss, nbinsx=80, name="TSS"))

# Overlay both histograms
fig.update_layout(barmode='overlay')
# Reduce opacity to see both histograms
fig.update_traces(opacity=0.75)
fig.write_html("MCF7-DRIP-Mutations/tss_tts_rloops_mutations.html")

#drip_all_df = pd.DataFrame(drip_all, columns=[["Chr", "Start", "End", "Mutations"]])
#drip_tss_df = pd.DataFrame(drip_tss, columns=[["Chr", "Start", "End", "Mutations"]])
#drip_tts_df = pd.DataFrame(drip_tts, columns=[["Chr", "Start", "End", "Mutations"]])

#drip_all_df.to_csv("Annotations/MCF7/All/drip_all_mck.tsv", sep="\t", index=False)
#drip_tss_df.to_csv("Annotations/MCF7/TSS/drip_tss_mck.tsv", sep="\t", index=False)
#drip_tts_df.to_csv("Annotations/MCF7/TTS/drip_tts_mck.tsv", sep="\t", index=False)