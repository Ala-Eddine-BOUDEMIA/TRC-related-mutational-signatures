import pandas as pd 
import plotly.express as px

utrs3 = pd.read_csv("Annotations/ucsc_3utr.tsv", header=0, sep="\t")
utrs5 = pd.read_csv("Annotations/ucsc_5utr.tsv", header=0, sep="\t")
utrs3["Length"] = utrs3["End"] - utrs3["Start"]
utrs5["Length"] = utrs5["End"] - utrs5["Start"]
utrs3.describe().to_csv(
	"Annotations/Statistical_Description/TSV/ucsc_3utr_summary.tsv", sep="\t")
utrs5.describe().to_csv(
	"Annotations/Statistical_Description/TSV/ucsc_5utr_summary.tsv", sep="\t")

hist_3utr = px.histogram(utrs3, x="Length", 
	range_x = [0,2000], title="Length of 3'UTR")
hist_3utr.show()
hist_3utr.write_html("Annotations/Statistical_Description/HTML/hist_ucsc_3utr.html")

hist_5utr = px.histogram(utrs5, x="Length",
	range_x = [0,2000], title="Length of 5'UTR")
hist_5utr.show()
hist_5utr.write_html("Annotations/Statistical_Description/HTML/hist_ucsc_5utr.html")
