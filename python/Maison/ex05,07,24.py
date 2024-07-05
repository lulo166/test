def effectif_notes(notes_eval):
    effectif = [0]*11
    for i in range(0, 11):
        for j in range(0, len(notes_eval)):
            if notes_eval[j] == i:
                effectif[i] += 1
    return effectif


notes_eval = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert effectif_notes(notes_eval) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def notes_triees(effectif_notes):
    notes = []
    niv_notes = 0
    for i in range(0, len(effectif_notes)):
        for j in range(0, effectif_notes[i]):
            notes.append(niv_notes)
        niv_notes += 1
    return notes

assert notes_triees([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r) 
    else:
        return dec_to_bin(q) + str(r)

assert dec_to_bin(10) == '1010'

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

assert bin_to_dec('1010') == 10