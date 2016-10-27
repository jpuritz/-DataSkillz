my_dna = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'

frag1 = my_dna.find('GAATTC')
frag2 = len(my_dna) - frag1

print("fragment 1 = " + str(frag1))
print("fragment 2 = " + str(frag2))
