mots ='FLORES ASTRILD CLAPET NOIRCIR FORGES COFFRET CREPES POULAIN HANSES POIGNET'
a = 0
b = len(mots)
toto=''
for i in range(0, int(len(mots)/2)):
    if (mots[i]==' '):
        toto = toto + mots[abs(a-b)]
    a = a + 2
    b = b - 1
print(toto)