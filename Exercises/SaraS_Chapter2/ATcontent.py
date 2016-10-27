dna_seq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

count_A = dna_seq.count('A')
count_T = dna_seq.count('T')
total_length = len(dna_seq)
percent_AT = (count_A + count_T)/total_length

print("count of A: " + str(count_A))
print("count of T: " + str(count_T))
print("percent_AT: " + str(percent_AT))
