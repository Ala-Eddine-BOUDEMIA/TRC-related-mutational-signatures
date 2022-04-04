#Scale Regions

computeMatrix scale-regions \
	--numberOfProcessors max --regionsFileName coding_genes_lft_hg19.bed \
	--beforeRegionStartLength 10000 --afterRegionStartLength 10000 --regionBodyLength 20000 \
	--binSize 500 --maxThreshold 1000 --minThreshold -100 --scoreFileName DRIP_HeLa.bw \
	--outFileName HeLa_DRIP_matrix.gz --missingDataAsZero --skipZeros

computeMatrix scale-regions \
	--numberOfProcessors max --regionsFileName coding_genes_lft_hg19.bed \
	--beforeRegionStartLength 10000 --afterRegionStartLength 10000 --regionBodyLength 20000 \
	--binSize 500 --maxThreshold 1000 --minThreshold -100  --scoreFileName pRPA_HeLa.bw \
	--outFileName HeLa_pRPA_matrix.gz --missingDataAsZero --skipZeros

computeMatrix scale-regions \
	--numberOfProcessors max --regionsFileName coding_genes_lft_hg19_plus.bed \
	--beforeRegionStartLength 10000 --afterRegionStartLength 10000 \
	--regionBodyLength 20000 --binSize 1000 --scoreFileName RFD_HeLa.bw \
	--outFileName HeLa_RFD_plus_matrix.gz --missingDataAsZero --skipZeros

computeMatrix scale-regions \
	--numberOfProcessors max --regionsFileName coding_genes_lft_hg19_minus.bed \
	--beforeRegionStartLength 10000 --afterRegionStartLength 10000 \
	--regionBodyLength 20000 --binSize 1000 --scoreFileName RFD_HeLa.bw \
	--outFileName HeLa_RFD_minus_matrix.gz --missingDataAsZero --skipZeros

plotProfile --matrixFile HeLa_DRIP_matrix.gz \
	--outFileName HeLa_DRIP.png --averageType mean \
	--samplesLabel HeLa-DRIP --startLabel TSS --endLabel TTS \
	--plotType se --legendLocation lower-right

plotProfile --matrixFile HeLa_pRPA_matrix.gz \
	--outFileName HeLa_pRPA.png --averageType mean \
	--samplesLabel HeLa-pRPA --startLabel TSS --endLabel TTS \
	--plotType se --legendLocation lower-right 

plotProfile --matrixFile HeLa_RFD_plus_matrix.gz \
	--outFileName HeLa_RFD_plus.png --averageType mean \
	--samplesLabel HeLa-RFD --startLabel TSS --endLabel TTS \
	--plotType se --legendLocation lower-right 

plotProfile --matrixFile HeLa_RFD_minus_matrix.gz \
	--outFileName HeLa_RFD_minus.png --averageType mean \
	--samplesLabel HeLa-RFD --startLabel TSS --endLabel TTS \
	--plotType se --legendLocation lower-right 