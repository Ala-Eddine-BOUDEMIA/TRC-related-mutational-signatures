import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff
from fitter import Fitter

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