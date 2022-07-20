mkdir -p Results/Matrices/reference-point/TSS/E2-2h
mkdir -p Results/Images/reference-point/TSS/E2-2h

folder = "MCF7_DRIP_Profiles/TSS/E2-2h/"

for f in $folder/*; do

	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";

	computeMatrix reference-point \
		--referencePoint TSS -b 5000 -a 5000 \
	    -R MCF7_DRIP_Profiles/Datasets/coding_genes_hg38_NOV_0kb.bed -S f \
	    --skipZeros -o Results/Matrices/reference-point/$filename_flat"_matrix.gz" \
	    --outFileSortedRegions Results/Matrices/reference-point/$filename_flat"_genes.bed"

	plotProfile --matrixFile Results/Matrices/reference-point/$filename_flat"_matrix.gz" \
		--outFileName Results/Images/reference-point/$filename_flat".png" --averageType sum \
		--samplesLabel $filename_flat \
		--plotType se --legendLocation best --perGroup