def verifie(tab):
    false = 0
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            false += 1
    if false > 0:
        return False
    else:
        return True

def verifie(tab):
    return True if all(tab[i] >= tab[i-1] for i in range(1, len(tab))) else False

assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([]) == True
assert verifie([5]) == True

print(verifie([2, 3, 3]))