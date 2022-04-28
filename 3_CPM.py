import numpy as np
import pandas as pd
import plotly.express as px

import Config 

def cpm(cancer, metadata):

    counts = pd.read_csv("Data/" + cancer + "/Transcriptomics/" + cancer.lower() + ".tsv", 
        header = 0, index_col = 0, sep = '\t')

    metadata = pd.read_csv(metadata, header=0, index_col="gdc_file_id", sep="\t")
    metadata.index = metadata.index.str.upper()

    counts = counts.T
    counts = counts.join(metadata['gdc_cases.samples.sample_type'])
    counts = counts[counts['gdc_cases.samples.sample_type'] == 'Primary Tumor']
    counts.pop('gdc_cases.samples.sample_type')
    counts = counts.T

    for i in counts.index.to_list():
        counts.rename(index = {i: i.split('.')[0]}, inplace = True)

    # Sum of counts per sample
    counts_per_sample = counts.sum(axis = 0)

    # cpm
    total = counts_per_sample.div(1e6)
    cpm = counts.loc[:,:].div(total) 
    cpm['Average_expression'] = cpm.mean(axis = 1)

    active_genes = cpm[cpm["Average_expression"] >= 1].index
    inactive_genes = cpm[cpm["Average_expression"] < 1].index

    fig = px.box(cpm, y="Average_expression")
    fig.show()
    fig = px.box(np.log10(cpm+1), y="Average_expression")
    fig.show()

    pd.Series(active_genes).to_csv("Annotations/" + cancer + "/Active_genes/all_active_genes.tsv", sep = "\t", index = False)
    pd.Series(inactive_genes).to_csv("Annotations/" + cancer + "/Inactive_genes/all_inactive_genes.tsv", sep = "\t", index = False)

if __name__ == '__main__':
    
    cpm(
        cancer = Config.args.cancer_type,
        metadata = Config.args.meta)