python3 make_bedGraph.py

region="TTS"
E2="E2-2h"
FOLDER="PCAWG_MCF7_DRIP_Profiles/"$region"/"$E2

for f in $FOLDER/*; do

	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";
	
	bedtools merge -i $f -c 4 -o sum > "PCAWG_MCF7_DRIP_Profiles/"$region"/"$E2"/"$filename_flat"_merged."$extension; 
	rm $f
	
done;

for f in $FOLDER/*; do

	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";
	
	./bedGraphToBigWig $f hg38.chrom.sizes "PCAWG_MCF7_DRIP_Profiles/"$region"/"$E2"/"$filename_flat".bw";
	rm $f;
done;