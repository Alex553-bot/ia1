import random
num = 0

def lanzarDados():
    return random.randint(1, 6), random.randint(1, 6)
def lanzarDado():
    return random.randint(1, 6)

def jugar():
    costo = 0
    res = 0
    print(f"Lanzamiento de los dados")
    dado1, dado2 = lanzarDados()
    res = (dado1-2)+(dado2-1)
    
    print(f"Resultados de los dados del jugador: [{dado1}, {dado2}]  -> [2,1] --> ", res)
    costo = costo + 1
    while ([dado1, dado2] != [1, 2]) or ([dado1, dado2] != [2, 1]):
        # dado2 > dado1
        if (dado1 == 1 and dado2 != 2):
            num = dado1
            while (dado2 != 2):
                dado2 = lanzarDado()
                res = (num-1)+(dado2-2)
                print(f"Resultados de los dados del jugador: [{num}, {dado2}]  -> [1,2] --> ", res)
                costo = costo + 1
        # dado1 > dado2
        if (dado1 == 2 and dado2 != 1):
            num = dado1
            while (dado2 != 1):
                dado2 = lanzarDado()
                res = (num-2)+(dado2-1)
                print(f"Resultados de los dados del jugador: [{num}, {dado2}]  -> [2,1] --> ", res)
                costo = costo + 1
        # dado1 > dado2
        if (dado2 == 1 and dado1 != 2):
            num = dado2
            while (dado1 != 2):
                dado1 = lanzarDado()
                res = (dado1-2)+(num-1)
                print(f"Resultados de los dados del jugador: [{dado1}, {num}]  -> [2,1] --> ", res)
                costo = costo + 1
        # dado2 > dado1
        if (dado2 == 2 and dado1 != 1):
            num = dado2
            while (dado1 != 1):
                dado1 = lanzarDado()
                res = (dado1-1)+(num-2)
                print(f"Resultados de los dados del jugador: [{dado1}, {num}]  -> [1,2] --> ", res)
                costo = costo + 1

        if (res == 0):
            print(f"\nJugador gana")
            print(f"Costo: ", costo, "\n")
            break
        
        dado1, dado2 = lanzarDados()
        res = (dado1-2)+(dado2-1)
        print(f"Resultados de los dados del jugador: [{dado1}, {dado2}]  -> [2,1] --> ", res)
        costo = costo + 1

jugar()