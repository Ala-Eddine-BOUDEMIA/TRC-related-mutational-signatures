import numpy as np
import pandas as pd
import plotly.express as px

import Config 
import Tools

def cpm(dataset, metadata):

    counts = pd.read_csv("Data/" + dataset + "/Transcriptomics/" + dataset.lower() + ".tsv", 
        header = 0, index_col = 0, sep = '\t')

    counts = counts.T
    if metadata.split("/")[-2] == "PCAWG":
        metadata = pd.read_csv(metadata, header=0, index_col="aliquot_id", sep="\t")
        metadata.index = metadata.index.str.upper()
        counts = counts.join(metadata['histology_abbreviation'])
        counts = counts[counts['histology_abbreviation'] == 'Breast-AdenoCA']
        counts.pop('histology_abbreviation')
        
    elif metadata.split("/")[-2] == "TCGA":
        metadata = pd.read_csv(metadata, header=0, index_col="gdc_file_id", sep="\t")
        metadata.index = metadata.index.str.upper()
        counts = counts.join(metadata['gdc_cases.samples.sample_type'])
        counts = counts[counts['gdc_cases.samples.sample_type'] == 'Primary Tumor']
        counts.pop('gdc_cases.samples.sample_type')
    counts = counts.T

    for i in counts.index.to_list():
        if len(i.split(".")[1]) <= 2:
            counts.rename(index = {i: i.split('.')[0]}, inplace = True)
        else:
            pass

    counts_per_sample = counts.sum(axis = 0)

    total = counts_per_sample.div(1e6)
    cpm = counts.loc[:,:].div(total) 
    cpm['Average_expression'] = cpm.mean(axis = 1)

    fig = px.box(cpm["Average_expression"])
    fig.show()
    
    active_genes = cpm[cpm["Average_expression"] >= 0.1].index
    inactive_genes = cpm[cpm["Average_expression"] < 0.1].index

    for i in ["Active_genes", "Inactive_genes"]:
        Tools.create_folder("Annotations/" + dataset + "/" + i)

    pd.Series(active_genes).to_csv("Annotations/" + dataset + "/Active_genes/all_active_genes.tsv", sep = "\t", index = False)
    pd.Series(inactive_genes).to_csv("Annotations/" + dataset + "/Inactive_genes/all_inactive_genes.tsv", sep = "\t", index = False)

    cpm.to_csv("Data/" + dataset + "/Transcriptomics/" + dataset.lower() + "_normalized.tsv", sep = "\t", 
        float_format='%.3f')

if __name__ == '__main__':
    
    cpm(
        dataset = Config.args.dataset,
        metadata = Config.args.meta)