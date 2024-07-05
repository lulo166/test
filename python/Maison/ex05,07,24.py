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

