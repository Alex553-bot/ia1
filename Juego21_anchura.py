import random
 
def jugar(val1, val2):
    res = []
    jugar_recursivo(val1, val2, 0, 0, res, False)
    return res

def jugar_recursivo(val1, val2, dado1, dado2, res, bb):
    if dado1 == 0 and dado2 == 0:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
    else:
        bb = dado1 == val1 and dado2 == val2 or dado1 == val2 and dado2 == val1
        combinaciones(1, 1, dado1, dado2, res)
        dado1 = 0
        dado2 = 0
    if not bb:
        jugar_recursivo(val1, val2, dado1, dado2, res, bb)

def combinaciones(i, j, valord1, valord2, res):
    if i < 6:
        combinaciones(i+1, j, valord1, valord2, res)

    combinaciones2(i, j, valord1, valord2, res)

def combinaciones2(i, j, valord1, valord2, res):
    if j < 6:
        combinaciones2(i, j+1, valord1, valord2, res)

    if valord1 == i and valord2 == j:
        res.append((i, j))
        

print(jugar(2,1))