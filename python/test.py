def fusion(r1, r2):
  r0 = []
  for i in range(len(r1)):
    r0.append(r1)
  for i in range(len(r2)):
    r0.append(r2)
  resultat = []
  for i in range(len(r1)+len(r2)):
    plus_petit = r0[0]
    id = 0
    for j in range(len(r0)):
      if plus_petit > r0[j]:
        plus_petit = r0[j]
        id = j
    resultat.append(plus_petit)
    del r0[id]
  return resultat
