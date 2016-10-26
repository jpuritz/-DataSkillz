##Chapter 2 Exercises

###Computing environment

I did these exercises in ipython.  I am currently using [miniconda](http://conda.pydata.org/miniconda.html) to manage my computing environments.


`conda create --name snakes python=3`
`source activate snakes`
`conda install ipython`

My python version is:

`python --version`
```
Python 3.5.2 :: Continuum Analytics, Inc.
```


##Ex.1 Calculating AT content
Here's a short DNA sequence:
`ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT`
Write a program that will print out the AT content of this DNA sequence. Hint: you can use normal mathematical symbols like add (+), subtract (-), multiply (*), divide (/) and parentheses to carry out calculations on numbers in Python.

```python
DNA_SEQ="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
Total_Bases=len(DNA_SEQ)
AT=DNA_SEQ.count("A")+DNA_SEQ.count("T")
print("The AT Content is " + str(round(AT/Total_Bases * 100,2)) +  "%")
```
```
The AT Content is 68.52%
```

##Ex.2 Complementing DNA
Here's a short DNA sequence:
 `ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT`
Write a program that will print the complement of this sequence.

```python
DNA_SEQ="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print( DNA_SEQ.replace("A","X").replace("T","A").replace("X","T").replace("G","X").replace("C","G").replace("X","C"))
```

```
TGACTAGCTAATGCATATCATAAACGATAGTATGTATATATAGCTACGCAAGTA
```

##Ex.3 Restriction fragment lengths
Here's a short DNA sequence:
`ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT`
The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif `G*AATTC` (the position of the cut is indicated by an asterisk). Write a program which will calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI.

```python
DNA_SEQ="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
Frag1 = DNA_SEQ.find("GAATTC") + 1
print("Fragment 1 is " + str(Frag1) + " bp")
print("Fragment 2 is " + str(len(DNA_SEQ) - Frag1) + " bp")
```
```
Fragment 1 is 22 bp
Fragment 2 is 33 bp
```

##Ex.4 Splicing out introns, part one
Here's a short section of genomic DNA:
`ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT`
It comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third character, and the second exon runs from the ninety- first character to the end of the sequence. Write a program that will print just the coding regions of the DNA sequence.

```python
DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
print(DNA[0:64] + DNA[90:])
```
```
ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATATCATCGATCGATATCGATGCATCGACTACTAT
```

##Ex.5 Splicing out introns, part two

Using the data from part one, write a program that will calculate what percentage of the DNA sequence is coding.

```python
DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

Coding_Seq=DNA[0:62] + DNA[90:]

print( "The DNA sequence is " + str(round(len(Coding_Seq)/len(DNA)*100,2)) + " % coding")
```

```
The DNA sequence is 77.24 % coding
```

##Ex.6 Splicing out introns, part three
Using the data from part one, write a program that will print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.

```python
DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

print(DNA[0:62] + DNA[62:90].lower() + DNA[90:])
```

```
ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGatcgatcgatcgatcgatcgatcatgctATCATCGATCGATATCGATGCATCGACTACTAT
```