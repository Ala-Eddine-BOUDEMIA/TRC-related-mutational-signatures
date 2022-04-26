import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("--cancer_type", 
	type = str,
	default = "BRCA",
	help = "Dataset to use")

parser.add_argument("--region",
	type = str,
	default = "TSS",
	help = "TSS, TTS or Remain")

parser.add_argument("--gff3", 
	type = Path,
	default = Path("Annotations/grch38.gff3"),
	help = "GRCh38 gff3 annotation file")

parser.add_argument("--all_coding_genes", 
	type = Path,
	default = Path("Annotations/coding_genes_hg38.bed"),
	help = "All coding genes extracted from the gff3 file")

parser.add_argument("--non_overlapping_genes", 
	type = Path,
	default = Path("Annotations/coding_genes_hg38_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes")

parser.add_argument("--non_overlapping_genes_plus", 
	type = Path,
	default = Path("Annotations/coding_genes_plus_hg38_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes located on the + strand")

parser.add_argument("--non_overlapping_genes_minus", 
	type = Path,
	default = Path("Annotations/coding_genes_minus_hg38_NOV_0kb.bed"),
	help = "File containing only non-overlapping genes located on the - strand")

parser.add_argument("--tss", 
	type = Path,
	default = Path("Annotations/tss.tsv"),
	help = "All the TSS regions that were extracted from the coding genes")

parser.add_argument("--tts", 
	type = Path,
	default = Path("Annotations/tts.tsv"),
	help = "All the TTS regions that were extracted from the coding genes")

parser.add_argument("--cluster", 
	type = bool,
	default = True,
	help = "If running on the HPC or not")

parser.add_argument("--num_signatures", 
	type = int,
	default = 5,
	help = "The maximum number of mutational signatures to be extracted")

args = parser.parse_args()