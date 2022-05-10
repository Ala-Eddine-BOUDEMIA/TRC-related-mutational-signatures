import pandas as pd 

import Config

cancer = Config.args.cancer_type
tss = pd.read_csv("MAF_Analysis/" + cancer + "/Summaries/TSS/6kb/" + cancer.lower() + "-tss-6kb_geneSummary.txt", index_col = 0, sep = "\t")
tts = pd.read_csv("MAF_Analysis/" + cancer + "/Summaries/TTS/6kb/" + cancer.lower() + "-tts-6kb_geneSummary.txt", index_col = 0, sep = "\t")

intersection = tss.index.intersection(tts.index)

print(len(intersection))

pd.Series(intersection).to_csv("TSS-TTS-6kb.tsv", sep = "\t")