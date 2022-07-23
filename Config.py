import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

hg = "hg37"
grch = "GRCh37"
metadata = "PCAWG"

parser.add_argument("--dataset", 
	type = str,
	default = "PCAWG_BRCA",
	help = "Dataset to use")

parser.add_argument("--num_signatures", 
	type = int,
	default = 5,
	help = "The maximum number of mutational signatures to be extracted")

parser.add_argument("--state", 
	type = str,
	default = "All",
	help = "active, inactive, 6kb")

parser.add_argument("--cluster", 
	action = "store_true",
	default = False,
	help = "If running on the HPC or not")

parser.add_argument("--strand", 
	action = "store_true",
	default = False,
	help = "If True, consider overlapping genes on different strands")

parser.add_argument("--region",
	type = str,
	default = "TSS",
	help = "TSS, TTS or Remain")

parser.add_argument("--meta",
	type = Path,
	default = Path("Annotations/Metadata/" + metadata + "/" + metadata + ".tsv"),
	help = "Metadata about RNA-seq from " + metadata)

parser.add_argument("--gff3", 
	type = Path,
	default = Path("Annotations/" + hg + "/gff3/" + grch.lower() + ".gff3"),
	help = grch + " gff3 annotation file")

parser.add_argument("--protein_coding_genes", 
	type = Path,
	default = Path("Annotations/" + hg + "/All_protein_coding_genes/coding_genes_" + hg + ".bed"),
	help = "All coding genes extracted from the gff3 file")

parser.add_argument("--non_overlapping_genes", 
	type = Path,
	default = Path("Annotations/" + hg + "/non-overlapping_coding_genes/coding_genes_" + hg + "_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes")

parser.add_argument("--non_overlapping_genes_plus", 
	type = Path,
	default = Path("Annotations/" + hg + "/non-overlapping_coding_genes/coding_genes_plus_" + hg + "_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes located on the + strand")

parser.add_argument("--non_overlapping_genes_minus", 
	type = Path,
	default = Path("Annotations/" + hg + "/non-overlapping_coding_genes/coding_genes_minus_" + hg + "_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes located on the - strand")

parser.add_argument("--tss", 
	type = Path,
	default = Path("Annotations/" + hg + "/TSS/tss.tsv"),
	help = "All the TSS regions that were extracted from the coding genes")

parser.add_argument("--tts", 
	type = Path,
	default = Path("Annotations/" + hg + "/TTS/tts.tsv"),
	help = "All the TTS regions that were extracted from the coding genes")

parser.add_argument("--active_genes", 
	type = Path,
	default = Path("Annotations/" + parser.parse_args().dataset + "/Active_genes/active_coding_genes.tsv"),
	help = "The protein coding genes that are active in a given cancer type")

parser.add_argument("--inactive_genes", 
	type = Path,
	default = Path("Annotations/" + parser.parse_args().dataset + "/Inactive_genes/inactive_coding_genes.tsv"),
	help = "The protein coding genes that are inactive in a given cancer type")

parser.add_argument("--active_tss", 
	type = Path,
	default = Path("Annotations/" + parser.parse_args().dataset + "/TSS/active_tss.tsv"),
	help = "All the TSS regions that were extracted from the active coding genes")

parser.add_argument("--inactive_tss", 
	type = Path,
	default = Path("Annotations/" + parser.parse_args().dataset + "/TSS/inactive_tss.tsv"),
	help = "All the TSS regions that were extracted from the inactive coding genes")

parser.add_argument("--active_tts", 
	type = Path,
	default = Path("Annotations/" + parser.parse_args().dataset + "/TTS/active_tts.tsv"),
	help = "All the TTS regions that were extracted from the active coding genes")

parser.add_argument("--inactive_tts", 
	type = Path,
	default = Path("Annotations/" + parser.parse_args().dataset + "/TTS/inactive_tts.tsv"),
	help = "All the TTS regions that were extracted from the inactive coding genes")

parser.add_argument("--conv", 
	type = Path,
	default = Path("Annotations/" + hg + "/Convergent_genes/conv_genes.tsv"),
	help = "Gene pairs in a convergent orientation")

parser.add_argument("--div", 
	type = Path,
	default = Path("Annotations/" + hg + "/Divergent_genes/div_genes.tsv"),
	help = "Gene pairs in a divergent orientation")

parser.add_argument("--tand", 
	type = Path,
	default = Path("Annotations/" + hg + "/Tandem_genes/co_genes.tsv"),
	help = "Gene pairs in a co-directional orientation")

args = parser.parse_args()