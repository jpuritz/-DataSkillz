# Chapter 3

##Ex.1 Splitting genomic DNA
Look in the chapter_3 folder for a file called genomic_dna.txt – it contains the same piece of genomic DNA that we were using in the final exercise from chapter 2. Write a program that will split the genomic DNA into coding and non-coding parts, and write these sequences to two separate files.

```python
my_file= open("./genomic_dna.txt")

dna_seq= my_file.read()

coding=open("./coding.txt", "w")

coding.write(dna_seq[0:62] + dna_seq[90:])

coding.close()

noncoding=open("./noncoding.txt", "w")

noncoding.write(dna_seq[62:90].upper())

noncoding.close()

```

##Ex.2

Write a program that will create a FASTA file for the following three sequences – make sure that all sequences are in upper case and only contain the bases A, T, G and C.

|Sequence header|DNA sequence|
|---------------|------------|
|ABC123|ATCGTACGATCGATCGATCGCTAGACGTATCG|
|DEF456|actgatcgacgatcgatcgatcacgact|
|HIJ789|ACTGAC-ACTGT--ACTGTA----CATGTG|


```python
head1 = "ABC123"
head2 = "DEF456"
head3 = "HIJ789"
seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG" 
seq2 = "actgatcgacgatcgatcgatcacgact" 
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

my_fasta=open("./THE_FASTA.fa","w")

my_fasta.write(">" + head1 + '\n')
my_fasta.write(seq1 + '\n')
my_fasta.write(">" + head2 + '\n')
my_fasta.write(seq2.upper() + '\n')
my_fasta.write(">" + head3 + '\n')
my_fasta.write(seq3.replace("-","") + '\n')

my_fasta.close()
```
