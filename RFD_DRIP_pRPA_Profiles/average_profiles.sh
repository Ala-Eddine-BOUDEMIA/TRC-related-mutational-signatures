#Scale Regions

computeMatrix scale-regions \
	--numberOfProcessors max \
	--regionsFileName Datasets/coding_genes_hg19_NOV_0kb.bed \
	--beforeRegionStartLength 10000 --afterRegionStartLength 10000 \
	--regionBodyLength 20000 --binSize 500 --maxThreshold 1000 \
	--minThreshold -100 --scoreFileName DRIP_HeLa.bw pRPA_HeLa.bw\
	--outFileName Results/Matrices/scale-region/HeLa_DRIP_pRPA_matrix.gz \
	--missingDataAsZero --skipZeros

plotProfile --matrixFile Results/Matrices/scale-region/HeLa_DRIP_pRPA_matrix.gz \
	--outFileName Results/Images/scale-region/HeLa_DRIP_pRPA.png --averageType mean \
	--samplesLabel HeLa-DRIP HeLa-pRPA --colors red blue --startLabel TSS --endLabel TTS \
	--plotType se --legendLocation lower-right --perGroup 

computeMatrix scale-regions \
	--numberOfProcessors max \
	--regionsFileName Datasets/coding_genes_plus_hg19_NOV_0kb.bed \
	--beforeRegionStartLength 10000 --afterRegionStartLength 10000 \
	--regionBodyLength 20000 --binSize 1000 --scoreFileName RFD_HeLa.bw \
	--outFileName Results/Matrices/scale-region/HeLa_RFD_plus_matrix.gz \
	--missingDataAsZero --skipZeros

plotProfile --matrixFile Results/Matrices/scale-region/HeLa_RFD_plus_matrix.gz \
	--outFileName Results/Images/scale-region/HeLa_RFD_plus.png --averageType mean \
	--samplesLabel HeLa-RFD --startLabel TSS --endLabel TTS --plotType se \
	--legendLocation best --perGroup 

computeMatrix scale-regions \
	--numberOfProcessors max \
	--regionsFileName Datasets/coding_genes_minus_hg19_NOV_0kb.bed \
	--beforeRegionStartLength 10000 --afterRegionStartLength 10000 \
	--regionBodyLength 20000 --binSize 1000 --scoreFileName RFD_HeLa.bw \
	--outFileName Results/Matrices/scale-region/HeLa_RFD_minus_matrix.gz \
	--missingDataAsZero --skipZeros

plotProfile --matrixFile Results/Matrices/scale-region/HeLa_RFD_minus_matrix.gz \
	--outFileName Results/Images/scale-region/HeLa_RFD_minus.png --averageType mean \
	--samplesLabel HeLa-RFD --startLabel TTS --endLabel TSS --plotType se \
	--legendLocation lower-right --perGroup 

#Reference point

computeMatrix reference-point \
	--referencePoint TSS -b 10000 -a 10000 \
    -R Datasets/coding_genes_hg19_NOV_0kb.bed -S DRIP_HeLa.bw pRPA_HeLa.bw \
    --skipZeros -o Results/Matrices/reference-point/HeLa_DRIP_pRPA_TSS_matrix.gz \
    --outFileSortedRegions Results/Matrices/reference-point/HeLa_DRIP_pRPA_TSS_genes.bed

plotProfile --matrixFile Results/Matrices/reference-point/HeLa_DRIP_pRPA_TSS_matrix.gz \
	--outFileName Results/Images/reference-point/HeLa_DRIP_pRPA_TSS.png --averageType mean \
	--samplesLabel HeLa-DRIP HeLa-pRPA --colors red blue \
	--plotType se --legendLocation lower-right --perGroup

computeMatrix reference-point \
	--referencePoint TES -b 10000 -a 10000 \
    -R Datasets/coding_genes_hg19_NOV_0kb.bed -S DRIP_HeLa.bw pRPA_HeLa.bw \
    --skipZeros -o Results/Matrices/reference-point/HeLa_DRIP_pRPA_TES_matrix.gz \
    --outFileSortedRegions Results/Matrices/reference-point/HeLa_DRIP_pRPA_TES_genes.bed

plotProfile --matrixFile Results/Matrices/reference-point/HeLa_DRIP_pRPA_TES_matrix.gz \
	--outFileName Results/Images/reference-point/HeLa_DRIP_pRPA_TES.png --averageType mean \
	--samplesLabel HeLa-DRIP HeLa-pRPA --colors red blue \
	--plotType se --legendLocation lower-right --perGroup

computeMatrix reference-point \
	--referencePoint TSS -b 10000 -a 10000 \
    -R Datasets/coding_genes_plus_hg19_NOV_0kb.bed -S RFD_HeLa.bw \
    --skipZeros -o Results/Matrices/reference-point/HeLa_RFD_plus_TSS_matrix.gz \
    --outFileSortedRegions Results/Matrices/reference-point/HeLa_RFD_plus_TSS_genes.bed

plotProfile --matrixFile Results/Matrices/reference-point/HeLa_RFD_plus_TSS_matrix.gz \
	--outFileName Results/Images/reference-point/HeLa_RFD_plus_TSS.png --averageType mean \
	--samplesLabel HeLa-RFD	--plotType se --legendLocation lower-right --perGroup

computeMatrix reference-point \
	--referencePoint TES -b 10000 -a 10000 \
    -R Datasets/coding_genes_plus_hg19_NOV_0kb.bed -S RFD_HeLa.bw \
    --skipZeros -o Results/Matrices/reference-point/HeLa_RFD_plus_TES_matrix.gz \
    --outFileSortedRegions Results/Matrices/reference-point/HeLa_RFD_plus_TES_genes.bed

plotProfile --matrixFile Results/Matrices/reference-point/HeLa_RFD_plus_TES_matrix.gz \
	--outFileName Results/Images/reference-point/HeLa_RFD_plus_TES.png --averageType mean \
	--samplesLabel HeLa-RFD	--plotType se --legendLocation lower-right --perGroup

computeMatrix reference-point \
	--referencePoint TSS -b 10000 -a 10000 \
    -R Datasets/coding_genes_minus_hg19_NOV_0kb.bed -S RFD_HeLa.bw \
    --skipZeros -o Results/Matrices/reference-point/HeLa_RFD_minus_TSS_matrix.gz \
    --outFileSortedRegions Results/Matrices/reference-point/HeLa_RFD_minus_TSS_genes.bed

plotProfile --matrixFile Results/Matrices/reference-point/HeLa_RFD_minus_TSS_matrix.gz \
	--outFileName Results/Images/reference-point/HeLa_RFD_minus_TSS.png --averageType mean \
	--samplesLabel HeLa-RFD	--plotType se --legendLocation lower-right --perGroup

computeMatrix reference-point \
	--referencePoint TES -b 10000 -a 10000 \
    -R Datasets/coding_genes_minus_hg19_NOV_0kb.bed -S RFD_HeLa.bw \
    --skipZeros -o Results/Matrices/reference-point/HeLa_RFD_minus_TES_matrix.gz \
    --outFileSortedRegions Results/Matrices/reference-point/HeLa_RFD_minus_TES_genes.bed

plotProfile --matrixFile Results/Matrices/reference-point/HeLa_RFD_minus_TES_matrix.gz \
	--outFileName Results/Images/reference-point/HeLa_RFD_minus_TES.png --averageType mean \
	--samplesLabel HeLa-RFD	--plotType se --legendLocation lower-right --perGroup