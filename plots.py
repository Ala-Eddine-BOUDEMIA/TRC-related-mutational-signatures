import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff
from fitter import Fitter

tss = pd.read_csv("Mutational_Signatures/BRCA/TSS/6kb/SBS96/Suggested_Solution/COSMIC_SBS96_Decomposed_Solution/Activities/COSMIC_SBS96_Activities.txt", sep="\t")
tts = pd.read_csv("Mutational_Signatures/BRCA/TTS/6kb/SBS96/Suggested_Solution/COSMIC_SBS96_Decomposed_Solution/Activities/COSMIC_SBS96_Activities.txt", sep="\t")

tss_f = Fitter(tss["SBS1"])
tss_ = tss_f.fit()
tss_.summary()

tts_f = Fitter(tts["SBS1"])
tts_ = tts_f.fit()
tts_.summary()
"""
import Config

meta = pd.read_csv(Config.args.meta, sep="\t")

meta_primary = meta[meta['gdc_cases.samples.sample_type'] == 'Primary Tumor']
meta_breast = meta_primary[meta_primary['gdc_cases.project.primary_site'] == 'Breast']
meta_breast["cgc_drug_therapy_drug_name"] = meta_breast["cgc_drug_therapy_drug_name"].str.upper()
meta_breast["cgc_drug_therapy_pharmaceutical_therapy_type"] = meta_breast["cgc_drug_therapy_pharmaceutical_therapy_type"].str.upper()
fig = px.histogram(meta_breast, "cgc_drug_therapy_drug_name", title="Drug Therapy")
fig.show()

fig = px.histogram(meta_breast, "cgc_drug_therapy_pharmaceutical_therapy_type", title="Drug Therapy Type")
fig.show()
"""