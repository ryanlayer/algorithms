def encode(data, code):
    bits = []

    curr_bit = 0
    curr_bit_i = 0

    for d in data:
        if curr_bit_i + code[d]['len'] > 32:
            bits.append(curr_bit)
            curr_bit = 0
            curr_bit_i = 0

        curr_bit_i = curr_bit_i + code[d]['len']
        curr_bit = (curr_bit << code[d]['len']) + code[d]['code']


    if curr_bit_i > 0:
        bits.append(curr_bit)

    return bits

kcnq2 = \
'AGGCGCCGAGGTGCGCGCGGAGCGAGGTGGCCGCAGCGTCTCCGCGCGCGGCCCAAGCCCGGCAGGAGTG' + \
'CGGAACCGCCGCCTCGGCCATGCGGCTCCCGGCCGGGGGGCCTGGGCTGGGGCCCGCGCCGCCCCCCGCG' + \
'CTCCGCCCCCGCTGAGCCTGAGCCCGACCCGGGGCGCCTCCCGCCAGGCACCATGGTGCAGAAGTCGCGC' + \
'AACGGCGGCGTATACCCCGGCCCGAGCGGGGAGAAGAAGCTGAAGGTGGGCTTCGTGGGGCTGGACCCCG' + \
'GCGCGCCCGACTCCACCCGGGACGGGGCGCTGCTGATCGCCGGCTCCGAGGCCCCCAAGCGCGGCAGCAT' + \
'CCTCAGCAAACCTCGCGCGGGCGGCGCGGGCGCCGGGAAGCCCCCCAAGCGCAACGCCTTCTACCGCAAG' + \
'CTGCAGAATTTCCTCTACAACGTGCTGGAGCGGCCGCGCGGCTGGGCGTTCATCTACCACGCCTACGTGT' + \
'GAGTGGCCGGCGGGGCCCCCGTGGCGACCCCCATGGCGACCCCCATCGGCGACCCCATCGGCGACCCCGG' + \
'CCAGGCTGGCTGCGGCGGGTTTGGCTCCCTGCCCCTGGGTCTGGGTCCGGGGCCGGCGCTCCCCGGCGGG' + \
'AGTGCTGGGCCGAGACCGGAGAGCGATTGTACAGCGCGCGGGCAGGAAGGATTCCGGGGTCGGGGCCGCT' + \
'CAGGTCGGGGTGGGGGCTCCAGGCCCGCAGGACAGAGACGTGCGGCCGCCCCAGCCCCCTCCTCAGCCTG' + \
'GGAGGCCCCTCCCCGCGGCCTCTGCGCCGAACAAAGGGCCGGCCGGGGAGGGACGGCGGCAGCGCTGGGT' + \
'CTGGACTCTCCGGGACTCTCGGGGACCCGCGGGGCTGGGGCCGCCCGACCAAGCGAGGGCGGGGGGGAGG' + \
'GGTCTGGCCTGTCCTCCGCCATCCTCCCGAGCCGCTCTCCCTCAGACTAGGGTGAGCTTCTGGGTTCCTG' + \
'AGATGGGGGAGGGGCCCTCCCATGACCCCCCCACCCCAGCCCGGGCTGAGCGCAGCTGTCTGTCCTGCCC' + \
'CCTCGGCGCCGACGCCCCTCCCTGGCCCCGCGAACCCCCTCAGCTCCTGCGCTCAGCTCCTGCGCTGTCC' + \
'CATCTCTGCAGCCGCCGGCCGCCCCCGTGCACATCCCGGGCTCAGGACCCCTCCTTGGCAGAGCGAGGCC' + \
'CGGGGGAGGGGCTGCGGCAGACCTGGGACCCCCAGCCCTGGGCCTGGAAGGGGCTGTCCCCTCTTCCCGG' + \
'GCGAGGCTCAGGGAACGGCTGCCTCCTGGGGCAGGGCTGGCGGGGGGCGGCCGAAGCCTGCGTCCGTGTG' + \
'CACCTGGGTGTTCGCATGTGGAATTGCACGGCCCGCTGCGTGTGCGGCCTGTGCGGCCGGTGTGCACAGC' + \
'CTCCCCGCGCCAGGGCGCTTGCTCTCCCATCCCAGCTGAACAAGGGACCCGCTGAGCTCCGGGACCGGCC' + \
'ATTTTGTGTGAGAGGCATTTTGGGATGGGAGTGAGGGGCAGACTGGTCACAAGCTGGTCGGGCGCCCACC' + \
'TGGGCCGAGAGGGGTGTGTGCCCCACGAGTGTGCCCCAGCCTGCGTGTGGCCTTGAGTGTGCCCTTAGCA' + \
'GACCCTCCGTGGACTGTGATATGAGAGGGTTCTGGGGTAGGGAGAAGATCCCAGAGGGAAATGCCAGGCC' + \
'GCTTACAGGGAGGGTGTCTCCGTGGAGGGCCCCTGGGCACCCAGCCTGGGACTCCCCAAGCAGAAGCTTC' + \
'TCCGACCTCCTGGGTCCTGGAAGCCCTGTGGCCCCCAGGAGGTGAGTCTAGCTTTTCCAGTCCAGGGTTC' + \
'ATTCCCGAATCCCCAGATGAGCTTCTGTGTTCTCAGGAATGGCCTCCCCTGATGGCCCCCACCTGGCTGG' + \
'GGGCCAAAGGGGCTCTTGGTGGGCCGGTACTGGTCAGCCAGGTCCCTGCCCAAGGTGACTCCCCGGAGGA' + \
'GGGTAGGATAGAACCCACCCCCACAACCCTCCTGCCCTGACAGCCTGGCCAGCGCCCCGCTCTGCGTCTG' + \
'ACCCAGGGTTGGTTCTGCTTTGAGTCCATGATCCAAGGGCCCAGCGTGGCTGTTCCTGAGGTTTCCCGTT' + \
'GGGTCAGCAGCTCTCCGCATGGCCGCCCCCTGCCTGGGCCTGCGTGGGTCAGCCCCTCTGTCTCTCCTTC'

fixed_code = { 'A':{'code':0,'len':2}, #00
               'C':{'code':1,'len':2}, #01
               'T':{'code':2,'len':2}, #10
               'G':{'code':3,'len':2}} #11

print(len(kcnq2)*8)

freq = {}
for d in kcnq2:
    if d not in freq:
        freq[d] = 0
    freq[d] = freq[d] + 1
print(freq)

fixed_encoded_kcnq2 = encode(kcnq2, fixed_code)

print(len(fixed_encoded_kcnq2)*32)

var_code = { 'A':{'code':7,'len':3}, #111
             'C':{'code':0,'len':1}, #01
             'T':{'code':6,'len':3}, #110
             'G':{'code':2,'len':2}} #10

var_encoded_kcnq2 = encode(kcnq2, var_code)

print(len(var_encoded_kcnq2)*32)
