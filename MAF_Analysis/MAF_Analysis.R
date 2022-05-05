library("NMF")
library("pheatmap")
library("maftools")
library("BSgenome.Hsapiens.UCSC.hg38")

cancer = read.maf(
  maf = '/Users/aboudemi/Documents/TRC-related-mutational-signatures/Data/BLCA/TSS/6kb/tss.maf')

write.mafSummary(maf = cancer, basename = 'blca-tss-6kb')

png('/Users/aboudemi/Documents/TRC-related-mutational-signatures/MAF_Analysis/BLCA/Plots/TSS/6kb/Summary.png', width = 1200, height = 800)
plotmafSummary(maf = cancer, addStat = "median", dashboard = TRUE)
dev.off()

png('/Users/aboudemi/Documents/TRC-related-mutational-signatures/MAF_Analysis/BLCA/Plots/TSS/6kb/TiTv.png', width = 1200, height = 800)
cancer.titv = titv(cancer, useSyn = TRUE)
dev.off()

png('/Users/aboudemi/Documents/TRC-related-mutational-signatures/MAF_Analysis/BLCA/Plots/TSS/6kb/Oncogenic_Pathways.png', width = 1200, height = 800)
OncogenicPathways(maf = cancer)
dev.off()

png('/Users/aboudemi/Documents/TRC-related-mutational-signatures/MAF_Analysis/BLCA/Plots/TSS/6kb/Mutational_Load.png', width = 1200, height = 800)
cancer.mutload = tcgaCompare(maf = cancer, cohortName = 'BLCA-TSS', logscale = TRUE, capture_size = 40)
dev.off()

cancer.tnm = trinucleotideMatrix(maf = cancer, add = TRUE, ref_genome = "BSgenome.Hsapiens.UCSC.hg38")

png('/Users/aboudemi/Documents/TRC-related-mutational-signatures/MAF_Analysis/BLCA/Plots/TSS/6kb/APOBEC_Enrichement.png', width = 1200, height = 800)
plotApobecDiff(tnm = cancer.tnm, maf = cancer, pVal = 0.05)
dev.off()

cancer.sign = estimateSignatures(mat = cancer.tnm, nTry = 13)

plotCophenetic(res = cancer.sign)

cancer.sig = extractSignatures(mat = cancer.tnm, n = 13)

cancer.og30.cosm = compareSignatures(nmfRes = cancer.sig, sig_db = "legacy")
cancer.v3.cosm = compareSignatures(nmfRes = cancer.sig, sig_db = "SBS")

maftools::plotSignatures(nmfRes = cancer.sig, title_size = 1.2, sig_db = "SBS")
