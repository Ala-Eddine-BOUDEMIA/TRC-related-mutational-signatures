library('recount', quietly = TRUE)

tcga = load("/Users/aboudemi/Documents/TRC-related-mutational-signatures/Data/BLCA/Transcriptomics/rse_gene_bladder.Rdata")

tcga_counts = assays(read_counts(rse_gene, use_paired_end = TRUE, round = TRUE))$counts

write.table(tcga_counts, file="/Users/aboudemi/Documents/TRC-related-mutational-signatures/Data/BLCA/Transcriptomics/blca.tsv", sep="\t")
