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

df["Direction"] = df["Strand_gene1"] + df["Strand_gene2"]
df["Region_Type"] = str
df["Mutation_Region_Start"] = 0
df["Mutation_Region_End"] = 0

selected = []
for i in df.index:
	if df.iloc[i]["Distance"] <= 10000:
		if df.iloc[i]["Direction"] == "+-":
			df.at[i, "Region_Type"] = "C"
			df.at[i, "Mutation_Region_Start"] = df.iloc[i]["End_gene1"] 
			df.at[i, "Mutation_Region_End"] = df.iloc[i]["End_gene2"]
		elif df.iloc[i]["Direction"] == "-+":
			df.at[i, "Region_Type"] = "D"
			df.at[i, "Mutation_Region_Start"] = df.iloc[i]["Start_gene1"] 
			df.at[i, "Mutation_Region_End"] = df.iloc[i]["Start_gene2"]
		elif df.iloc[i]["Direction"] == "++":
			df.at[i, "Region_Type"] = "T"
			df.at[i, "Mutation_Region_Start"] = df.iloc[i]["End_gene1"] 
			df.at[i, "Mutation_Region_End"] = df.iloc[i]["Start_gene2"]
		elif df.iloc[i]["Direction"] == "--":
			df.at[i, "Region_Type"] = "T"
			df.at[i, "Mutation_Region_Start"] = df.iloc[i]["Start_gene1"] 
			df.at[i, "Mutation_Region_End"] = df.iloc[i]["End_gene2"]

		if df.iloc[i]["Name_gene1"] not in selected:
			selected.append(df.iloc[i]["Name_gene1"])
		if df.iloc[i]["Name_gene2"] not in selected:
			selected.append(df.iloc[i]["Name_gene2"])
	else:
		df.at[i, "Region_Type"] = "A"

print(df)