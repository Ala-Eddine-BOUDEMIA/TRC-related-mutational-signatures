import pandas as pd

file_path = "/Users/aboudemi/Documents/TRC-related-mutational-signatures/Mutational_Signatures_V2/BRCA/"
file_path = file_path + "Divergent/All/SBS96/Suggested_Solution/COSMIC_SBS96_Decomposed_Solution/Activities/"
file_path = file_path + "COSMIC_SBS96_Activities.txt"

file = pd.read_csv(file_path, sep="\t", index_col=0)

sbs_total = file.sum(axis=0)
sbs_total = pd.DataFrame(sbs_total, index = file.columns, columns=["total"])
total = sbs_total["total"].sum()

sbs_total = sbs_total.div(total) * 100
print(total)
print(sbs_total)