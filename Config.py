import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("--dataset", 
	type = str,
	default = "BRCA",
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
	default = Path("Annotations/Metadata/PCAWG/PCAWG.tsv"),
	help = "Metadata about RNA-seq from PCAWG")

parser.add_argument("--gff3", 
	type = Path,
	default = Path("Annotations/hg37/gff3/grch37.gff3"),
	help = "GRCh37 gff3 annotation file")

parser.add_argument("--protein_coding_genes", 
	type = Path,
	default = Path("Annotations/hg37/All_protein_coding_genes/coding_genes_hg37.bed"),
	help = "All coding genes extracted from the gff3 file")

parser.add_argument("--non_overlapping_genes", 
	type = Path,
	default = Path("Annotations/hg37/non-overlapping_coding_genes/coding_genes_hg37_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes")

parser.add_argument("--non_overlapping_genes_plus", 
	type = Path,
	default = Path("Annotations/hg37/non-overlapping_coding_genes/coding_genes_plus_hg37_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes located on the + strand")

parser.add_argument("--non_overlapping_genes_minus", 
	type = Path,
	default = Path("Annotations/hg37/non-overlapping_coding_genes/coding_genes_minus_hg37_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes located on the - strand")

parser.add_argument("--tss", 
	type = Path,
	default = Path("Annotations/hg37/TSS/tss.tsv"),
	help = "All the TSS regions that were extracted from the coding genes")

parser.add_argument("--tts", 
	type = Path,
	default = Path("Annotations/hg37/TTS/tts.tsv"),
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
	default = Path("Annotations/hg38/Convergent_genes/conv_genes.tsv"),
	help = "Gene pairs in a convergent orientation")

parser.add_argument("--div", 
	type = Path,
	default = Path("Annotations/hg37/Divergent_genes/div_genes.tsv"),
	help = "Gene pairs in a divergent orientation")

parser.add_argument("--tand", 
	type = Path,
	default = Path("Annotations/hg37/Tandem_genes/co_genes.tsv"),
	help = "Gene pairs in a co-directional orientation")

args = parser.parse_args()