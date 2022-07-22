region="TTS"
E2="E2-2h"
folder="PCAWG_MCF7_DRIP_Profiles/"$region"/"$E2
rp=TES

mkdir -p PCAWG_MCF7_DRIP_Profiles/Results/Matrices/reference-point/$region/$E2
mkdir -p PCAWG_MCF7_DRIP_Profiles/Results/Images/reference-point/$region/$E2

for f in $folder/*; do

	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";

	computeMatrix reference-point \
		--referencePoint $rp -b 5000 -a 5000 -bs 100 \
	    -R "PCAWG_MCF7_DRIP_Profiles/Datasets/coding_genes_hg19_NOV_0kb.bed" -S $f \
	    --skipZeros -o "PCAWG_MCF7_DRIP_Profiles/Results/Matrices/reference-point/"$region"/"$E2"/"$filename_flat"_matrix.gz" \
	    --outFileSortedRegions "PCAWG_MCF7_DRIP_Profiles/Results/Matrices/reference-point/"$region"/"$E2"/"$filename_flat"_genes.bed";

	plotProfile --matrixFile "PCAWG_MCF7_DRIP_Profiles/Results/Matrices/reference-point/"$region"/"$E2/$filename_flat"_matrix.gz" \
		--outFileName "PCAWG_MCF7_DRIP_Profiles/Results/Images/reference-point/"$region"/"$E2"/"$filename_flat".png" --averageType sum \
		--samplesLabel Mutational_Rate \
		--plotType se --legendLocation best --perGroup;
	
done