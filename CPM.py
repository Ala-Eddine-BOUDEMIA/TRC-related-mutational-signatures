import pandas as pd
import plotly.express as px

import Config 

cancer = Config.args.cancer_type
counts = pd.read_csv("Data/" + cancer + "/Transcriptomics/" + cancer.lower() + ".tsv", 
    header = 0, index_col = 0, sep = '\t')

for i in counts.index.to_list():
    counts.rename(index = {i: i.split('.')[0]}, inplace = True)

# Sum of counts per sample
counts_per_sample = counts.sum(axis = 0)

# cpm
total = counts_per_sample.div(1e6)
cpm = counts.loc[:,:].div(total) 

cpm['Average_expression'] = cpm.mean(axis = 1)
active_genes = cpm[cpm["Average_expression"] >= 0.1].index
inactive_genes = cpm[cpm["Average_expression"] < 0.1].index

fig = px.box(cpm, y="Average_expression")
fig.show()

pd.Series(active_genes).to_csv(Config.args.all_active_genes, sep = "\t")
pd.Series(inactive_genes).to_csv(Config.args.all_inactive_genes, sep = "\t")