my_dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

exon_1 = my_dna[0:64]
exon_2 = my_dna[91:len(my_dna)]

print("Exon 1: " + str(exon_1))
print("Exon 2: " + str(exon_2))

perc_coding = ((len(exon_1) + len(exon_2))/(len(my_dna)))*100

print("Percent Coding: " + str(perc_coding))

intron_1 = my_dna[64:92]
intron_1 = intron_1.lower()

print(str(exon_1) + str(intron_1) + str(exon_2))