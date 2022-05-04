import pandas as pd

file = pd.read_csv("Data/BRCA/Original/brca.maf", header=5, sep="\t")

tcga = pd.read_csv("Annotations/Metadata/TCGA/TCGA.tsv", sep="\t")
tcga = tcga[tcga['gdc_cases.samples.sample_type']=="Primary Tumor"]
tcga = tcga[tcga['gdc_cases.project.primary_site']=="Breast"]

rna = tcga['gdc_cases.submitter_id'].str.split('-').str[2]
maf = file['Tumor_Sample_Barcode'].str.split("-").str[2]
intersection = pd.Series(list(set(rna).intersection(set(maf))))

print("Number of unique patients in the MAF file is: ", len(maf.unique()))
print("Number of unique patients in the RNA-Seq file is: ", len(rna.unique()))
print("Number of common patients between the files: ", len(intersection))