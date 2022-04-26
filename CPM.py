import pandas as pd

import Config 

cancer = Config.args.cancer_type
counts = pd.read_csv("Data/" + cancer + "/Transcriptomics/" + cancer.lower() + ".tsv", 
    header = 0, index_col = 0, sep = '\t')

for i in counts.index.to_list():
    counts.rename(index = {i: i.split('.')[0]}, inplace = True)

# Sum of counts per sample
counts_per_sample = counts.sum(axis = 0)
print(counts_per_sample)

# cpm
total = counts_per_sample.div(1e6)
cpm = counts.loc[:,:].div(total) 
print(cpm.sum(axis = 0))

cpm['Average_expression'] = cpm.mean(axis = 1)
active_genes = cpm[cpm["Average_expression"] > 0].index
inactive_genes = cpm.drop(active_genes, inplace = True).index

cpm.to_csv(Config.args.all_active_genes, sep = "\t")
cpm.to_csv(Config.args.all_inactive_genes, sep = "\t")