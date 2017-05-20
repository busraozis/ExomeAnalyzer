# ExomeAnalyzer

    * When writing the commands, please write the extension of input files in {} and for the output file [].
    Example: bwa mem -M -t 16 {fasta} {fastq.gz} {fastq.gz} > [sam]

    * If command includes any other reference files, apart from fasta and vcf's, please write its full path.
    Example: METRICS_FILE=/home/tolun/Desktop/metrics.txt

    * When adding new tool, you can write more than one command by seperating them with semicolon(;).
    Example: ./samtools view -bS {sam} > [bam] ; ./samtools sort {bam} [bam]

    * Please do not leave empty the 'Tool Name' and'Commands' section in Add New Tool. You can leave other parts empty.

    * If you are adding new executable file (like GenomeAnalysis.jar), please specify its full address.