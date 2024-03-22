def occurrences(caractere, chaine):
    num_de_lettre = 0
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            num_de_lettre += 1
    return num_de_lettre

assert occurrences('e', "science") == 2
assert occurrences('i', "mississipi") == 4
assert occurrences('a', "mississipi") == 0