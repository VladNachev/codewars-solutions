def dna_to_rna(dna):
    dna_array = [];
    for x in dna:
        if x == "T":
            dna_array.append("U");
        else:
           dna_array.append(x); 
           
    
    return ''.join(dna_array)