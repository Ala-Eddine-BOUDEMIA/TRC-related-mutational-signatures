import pandas as pd
import plotly.express as px

import Config

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

genes = pd.read_csv(Config.args.non_overlapping_genes, index_col = "ID", sep = "\t")

chromes = list(map(str,range(1,23)))+['X','Y']
chromes = ["chr" + x for x in chromes]
distances = {k:[] for k in chromes}

for x in chromes:
	chromosome = genes[genes["Chr"] == x]
	chromosome = chromosome.sort_values(["Start", "End"])
	for i in range(len(chromosome.index) - 1):
		dis = chromosome.iloc[i+1]["Start"] - chromosome.iloc[i]["End"]
		if dis >= 0:
			distances[x].append(list(chromosome.iloc[i]) + list(chromosome.iloc[i+1]) + [dis])

df = pd.DataFrame.from_dict(distances[chromes[0]])

for x in range(1, len(chromes)):
	df = pd.concat([df, pd.DataFrame.from_dict(distances[chromes[x]])], ignore_index = True)

df.columns = ["Chr", "Start_gene1", "End_gene1", "Name_gene1", 
	"Score_gene1", "Strand_gene1", "Length_gene1", "Chr_gene2", 
	"Start_gene2", "End_gene2", "Name_gene2", "Score_gene2", 
	"Strand_gene2", "Length_gene2", "Distance"]
df = df.drop(["Chr_gene2", "Score_gene2", "Score_gene1"], axis = 1)

df["Orientation"] = df["Strand_gene1"] + df["Strand_gene2"]
df["Region_Type"], df["Name"] = str, str
df["Start"], df["End"] = 0, 0
df["TSS_gene1"], df["TSS_gene2"] = 0, 0
df["TTS_gene1"], df["TTS_gene2"] = 0, 0

selected = []
for i in df.index:
	df.at[i, "Name"] = df.iloc[i]["Name_gene1"] + "-" + df.iloc[i]["Name_gene2"]
	if df.iloc[i]["Distance"] <= 10000:
		if df.iloc[i]["Orientation"] == "+-":
			df.at[i, "Region_Type"] = "C"
		elif df.iloc[i]["Orientation"] == "-+":
			df.at[i, "Region_Type"] = "D"
		elif df.iloc[i]["Orientation"] == "++":
			df.at[i, "Region_Type"] = "T"
		elif df.iloc[i]["Orientation"] == "--":
			df.at[i, "Region_Type"] = "T"
		df.at[i, "Start"] = df.iloc[i]["End_gene1"] - 3000
		df.at[i, "End"] = df.iloc[i]["Start_gene2"] + 3000
		"""
		if df.iloc[i]["Name_gene1"] not in selected:
			selected.append(df.iloc[i]["Name_gene1"])
		if df.iloc[i]["Name_gene2"] not in selected:
			selected.append(df.iloc[i]["Name_gene2"])
		"""
	else:
		df.at[i, "Region_Type"] = "A"

df = df[["Chr", "Start", "End", "Name", "Region_Type", "Orientation"]]
conv = df[df["Region_Type"] == "C"]
div = df[df["Region_Type"] == "D"]
tand = df[df["Region_Type"] == "T"]

conv.to_csv(Config.args.conv, 
	sep = "\t", index = False)
div.to_csv(Config.args.div, 
	sep = "\t", index = False)
tand.to_csv(Config.args.tand, 
	sep = "\t", index = False)