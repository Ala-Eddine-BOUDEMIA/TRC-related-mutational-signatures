import numpy as np
import pandas as pd
import plotly.express as px

import Config 

def cpm(dataset, metadata):

    counts = pd.read_csv("Data/" + dataset + "/Transcriptomics/" + dataset.lower() + ".tsv", 
        header = 0, index_col = 0, sep = '\t')

    metadata = pd.read_csv(metadata, header=0, index_col="gdc_file_id", sep="\t")
    metadata.index = metadata.index.str.upper()

    counts = counts.T
    counts = counts.join(metadata['gdc_cases.samples.sample_type'])
    counts = counts[counts['gdc_cases.samples.sample_type'] == 'Primary Tumor']
    counts.pop('gdc_cases.samples.sample_type')
    counts = counts.T

    for i in counts.index.to_list():
        if len(i.split(".")[1]) <= 2:
            counts.rename(index = {i: i.split('.')[0]}, inplace = True)
        else:
            pass

    # Sum of counts per sample
    counts_per_sample = counts.sum(axis = 0)

    # cpm
    total = counts_per_sample.div(1e6)
    cpm = counts.loc[:,:].div(total) 
    cpm['Average_expression'] = cpm.mean(axis = 1)

    active_genes = cpm[cpm["Average_expression"] >= 1].index
    inactive_genes = cpm[cpm["Average_expression"] < 1].index
    """
    fig = px.box(cpm, y="Average_expression")
    fig.show()
    fig = px.box(np.log10(cpm+1), y="Average_expression")
    fig.show()
    """
    pd.Series(active_genes).to_csv("Annotations/" + dataset + "/Active_genes/all_active_genes.tsv", sep = "\t", index = False)
    pd.Series(inactive_genes).to_csv("Annotations/" + dataset + "/Inactive_genes/all_inactive_genes.tsv", sep = "\t", index = False)

    cpm.to_csv("Data/" + dataset + "/Transcriptomics/" + dataset.lower() + "_normalized.tsv", sep = "\t", 
        float_format='%.3f')

if __name__ == '__main__':
    
    cpm(
        dataset = Config.args.dataset,
        metadata = Config.args.meta)