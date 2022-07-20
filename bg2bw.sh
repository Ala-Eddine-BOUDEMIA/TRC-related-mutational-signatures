python3 make_bedGraph.py

folder = "MCF7_DRIP_Profiles/TSS/E2-2h/"

for f in $folder/*; do
	
	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";
	
	bedtools merge -i f -c 4 -o sum > $filename_flat"_merged."$extension; 
	rm f;

done;

for f in $folder/*; do

	filename=$(basename -- "$f");
	extension="${filename##*.}";
	filename_flat="${filename%.*}";
	
	bedGraphToBigWig f hg38.chrom.sizes $filename_flat".bw";
	rm f;

done;