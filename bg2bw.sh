python3 make_bedGraph.py

FOLDER="MCF7_DRIP_Profiles/TSS/E2-2h"

for f in $FOLDER/*; do

	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";
	
	bedtools merge -i $f -c 4 -o sum > "MCF7_DRIP_Profiles/TSS/E2-2h/"$filename_flat"_merged."$extension; 
	rm $f
	
done;

for f in $FOLDER/*; do

	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";
	
	./bedGraphToBigWig $f hg38.chrom.sizes "MCF7_DRIP_Profiles/TSS/E2-2h/"$filename_flat".bw";
	rm $f;
done;