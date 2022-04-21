#programs on cluster
kdi='/data/kdi_prod/bin/kdi_analyse'
bowtie2="/bioinfo/local/build/Centos/bowtie2/bowtie2-2.2.9"
bcl2fastq2="/bioinfo/local/build/Centos/bcl2fastq/bcl2fastq2-v2.20/bin"
bamtools="/bioinfo/local/build/Centos/bamtools/bamtools-2.5.1/bin"
bedtools="/bioinfo/local/build/Centos/bedtools/bedtools-2.27.1/bin"
bismark="/bioinfo/local/build/Centos/Bismark/bismark_v0.21.0"
fastqc="/bioinfo/local/build/Centos/FastQC/FastQC_v0.11.5"
sratoolkit="/bioinfo/local/build/Centos/sratoolkit/sratoolkit-2.9.6-1/bin"
samtools="/bioinfo/local/build/Centos/samtools/samtools-1.9/bin"
STAR="/bioinfo/local/build/Centos/STAR/STAR-2.7.0e/bin/Linux_x86_64"
trimgalore="/bioinfo/local/build/Centos/trim_galore/trim_galore_v0.4.4"
bwa="/bioinfo/local/build/bwa-0.7.5a/bin"
cutadapt="/bioinfo/local/build/cutadapt-1.3/bin/"
macs2="/bioinfo/local/build/MACS2_2.0.10/bin"

export PATH="$Kronos:$kdi:$cutadapt:$bwa:$trimgalore:$fastqc:$macs2:$bowtie2:$bcl2fastq2:$subsetbam:$bismark:$samtools:$STAR:$sratoolkit:$bamtools:$bedtools:$PATH"
export PATH=/bioinfo/local/build/Centos/python/python-3.9.5/bin:$PATH
export LD_LIBRARY_PATH=/bioinfo/local/build/Centos/python/python-3.9.5/lib64

alias ll='ls -lGh --color=auto'
alias ls='ls --color=auto'
alias qstat='qstat -a'
alias nano='nano -\$cwS'
