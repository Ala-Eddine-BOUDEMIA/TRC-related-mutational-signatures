import pandas as pd 
import seaborn as sns

import Config

dataset = Config.args.dataset
path = "path"
signatures = pd.read_csv(path, index_col=0, sep="\t")
signatures = signatures.append(pd.Series(signatures.mean(), name="mean"))
signatures = signatures - signatures.loc["mean",:]
signatures = signatures.append(pd.Series(signatures.var(), name="var"))
signatures = signatures.div(signatures.loc["var",:])
signatures = signatures.drop("mean", axis=0)
signatures = signatures.drop("var", axis=0)

g = sns.clustermap(signatures,
	vmin = min(signatures.min()), 
	vmax = max(signatures.max()), 
	cmap = "Blues", metric = "euclidean",
	xticklabels = True, yticklabels = False,
	method = "ward")

g.savefig("img.png", dpi = 300)