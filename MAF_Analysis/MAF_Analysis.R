library("NMF")
library("pheatmap")
library("maftools")
library("BSgenome.Hsapiens.UCSC.hg38")

cancer = read.maf(
  maf = '/Users/aboudemi/Documents/TRC-related-mutational-signatures/Data/BLCA/TTS/6kb/tts.maf')

write.mafSummary(maf = cancer, basename = 'blca-tts-6kb')

plotmafSummary(maf = cancer, addStat = "median", dashboard = TRUE)

cancer.titv = titv(cancer, useSyn = TRUE)

OncogenicPathways(maf = cancer)

cancer.mutload = tcgaCompare(maf = cancer, cohortName = 'BLCA-TTS-6kb', logscale = TRUE, capture_size = 40)

cancer.tnm = trinucleotideMatrix(maf = cancer, add = TRUE, ref_genome = "BSgenome.Hsapiens.UCSC.hg38")

plotApobecDiff(tnm = cancer.tnm, maf = cancer, pVal = 0.05)

cancer.sign = estimateSignatures(mat = cancer.tnm, nTry = 13)

plotCophenetic(res = cancer.sign)

cancer.sig = extractSignatures(mat = cancer.tnm, n = 13)

cancer.og30.cosm = compareSignatures(nmfRes = cancer.sig, sig_db = "legacy")
cancer.v3.cosm = compareSignatures(nmfRes = cancer.sig, sig_db = "SBS")

maftools::plotSignatures(nmfRes = cancer.sig, title_size = 1.2, sig_db = "SBS")
