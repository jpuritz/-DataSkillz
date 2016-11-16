#Chapter 4

##Ex.1

Processing DNA in a file
The file input.txt contains a number of DNA sequences, one per line. Each sequence starts with the same 14 base pair fragment – a sequencing adapter that should have been removed. Write a program that will (a) trim this adapter and write the cleaned sequences to a new file and (b) print the length of each sequence to the screen.

```python
my_file=open("./input.txt")
my_output=open("./output.txt","w")

for line in my_file:
  line_length=len(line)
  my_output.write(line[15:line_length] + '\n')
  print("Length is " + str(len(line[15:line_length])))
my_output.close()
```

##Ex.2
The file genomic_dna.txt contains a section of genomic DNA, and the file exons.txt contains a list of start/stop positions of exons. Each exon is on a separate line and the start and stop positions are separated by a comma. Write a program that will extract the exon segments, concatenate them, and write them to a new file.

```python
seqs=open("./genomic_dna.txt")

actual_seq=seqs.read()

exons=open("./exons.txt")
out=open("./output2.txt","w")

for line in exons:
  ex_in=line.split(",")
  out.write(actual_seq[int(ex_in[0]):int(ex_in[1])])
  
out.close()
```

