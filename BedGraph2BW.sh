sort -k1,1 -k2,2n file.bedGraph > sorted_file.bedGraph
bedtools merge -i sorted_file -c 4 -o sum > file_nov.bedGraph
bedGraphToBigWig file_nov.bedGraph hg38.chrom.sizes file.bw