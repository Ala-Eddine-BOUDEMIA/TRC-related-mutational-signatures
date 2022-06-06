import pandas as pd

from scipy.stats import kruskal

def same_group():

	for dataset in ["BRCA", "BLCA"]:
		path1 = "Mutational_Signatures/" + dataset + "/Remain/inactive/SBS96/"
		path2 = "Suggested_Solution/COSMIC_SBS96_Decomposed_Solution/Activities/"
		name = "COSMIC_SBS96_Activities.txt"
		path = path1 + path2 + name

		signatures = pd.read_csv(path, index_col=0, sep="\t")
		cols = signatures.columns
		results = []
		for i in range(len(cols)):
			for j in range(i+1,len(cols)):
				h, p = kruskal(signatures[cols[i]], signatures[cols[j]])
				if p < 0.05:
					decision = "Rank medians are different"
				else:
					decision = "Rank medians are similar"

				results.append([cols[i], cols[j], 
					signatures[cols[i]].mean(), signatures[cols[j]].mean(),
					h, p, decision])

		results_df = pd.DataFrame(results, columns=["A", "B", "Mean_A", "Mean_B", 
			"H-statistic", "P-value", "Decision"])

		results_df.to_csv("Kruskal/" + dataset + "/Remain/inactive/H-statistic.tsv", sep="\t")
		print(results_df)

def between_groups():

	for dataset in ["BRCA", "BLCA"]:
		path0 = "Mutational_Signatures/" + dataset + "/Divergent/All/SBS96/"
		path1 = "Mutational_Signatures/" + dataset + "/Co-directional/All/SBS96/"
		path2 = "Suggested_Solution/COSMIC_SBS96_Decomposed_Solution/Activities/"
		name = "COSMIC_SBS96_Activities.txt"
		path_group1 = path0 + path2 + name
		path_group2 = path1 + path2 + name

		group1 = pd.read_csv(path_group1, index_col=0, sep="\t")
		group2 = pd.read_csv(path_group2, index_col=0, sep="\t")
		
		cols1 = group1.columns
		cols2 = group2.columns
		results = []
		for i in cols1:
			for j in cols2:
				if i == j:
					h, p = kruskal(group1[i], group2[j])
					if p < 0.05:
						decision = "Rank medians are different"
					else:
						decision = "Rank medians are similar"

					results.append([i, j, group1[i].mean(), group2[j].mean(),
						h, p, decision])

		results_df = pd.DataFrame(results, columns=["Divergent", "Co-directional", 
			"Mean_Divergent", "Mean_Co-directional", 
			"H-statistic", "P-value", "Decision"])

		results_df.to_csv("Kruskal/" + dataset \
			+ "/VS/Divergent-vs-Co-directional/H-statistic.tsv", sep="\t")
		print(results_df)


if __name__ == '__main__':
	#same_group()
	between_groups()