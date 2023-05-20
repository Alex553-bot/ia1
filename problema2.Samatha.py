import sys; 
INF = sys.maxsize

def nt(n): 
    return (1<<n)-1-n

def heuristica(s, t):
    n = len(s)
    m = len(t)
    dp = []
    for i in range(0, 2):
        a = []
        for j in range(0, n+1): 
            if (i&1): a.append(0)
            else: a.append(j)
        dp.append(a)

    for i in range(0, m): 
        x = (i&1)
        dp[x^1][0] = i+1;
        for j in range(1, n+1): 
            dp[x^1][j] = min(dp[x^1][j-1], dp[x][j])+1
            dp[x^1][j] = min(dp[x^1][j], dp[x][j-1] + (0 if t[i]==s[j-1] else 1))
    return dp[m&1][n]

pais    = 'Canada'
ciudad  = 'Toronto'
nombre  = 'Samantha Wilder'

def nodo(s, x): 
    st = 'Nodo actual visitando: '+s
    st += ' calculo de su heuristica: '+str(x)
    return st

def mejor(s):
    st = '***'*20
    st+='\n'
    st += 'Ruta de minimo coste seleccionada: \n'
    for a in s:
        st+=a+'\n'
    return st

def rutas2(s):
    st = '***'*20
    st+='\n'
    st += 'Rutas del pais: \n'
    for a in s:
        st+=a+'\n'
    return st

def solucion_avara(estante): 
    maximo = INF
    mejor_pais = ''
    mejor_ciudad = ''
    mejor_solucion = ''
    for pais_actual in estante:
        x = heuristica(pais, pais_actual)
        if x<maximo :
            mejor_pais = pais_actual
            maximo = x
        print(nodo(pais_actual, x))
    
    print("\n************************************************************")
    print("Rutas de las ciudades de cada pais")
    maximo2 = INF
    for pais_actual2 in estante:
        print(rutas2([pais_actual2]))
        for ciudad_actual2 in estante[pais_actual2]:    
            y = heuristica(ciudad, ciudad_actual2);
            if y<maximo2:
                maximo2 = y
            print(nodo(ciudad_actual2,y))
    
    print("\nRutas de los nombres de personas de las ciudades de cada pais")
    maximo3 = INF
    for pais_actual3 in estante:
        print(rutas2([pais_actual3]))
        for ciudad_actual3 in estante[pais_actual3]:    
            z = heuristica(ciudad, ciudad_actual3);
            if z<maximo3:
                maximo3 = z
            for nombre_actual3 in estante[pais_actual3][ciudad_actual3]:
                z = heuristica(nombre, nombre_actual3)
                if (z<maximo3):
                    maximo3 = z
                print("Ciudad: ", ciudad_actual3)
                print(nodo(nombre_actual3, z))
    print("\n************************************************************")

    print(mejor([mejor_pais]))
    maximo = INF
    for ciudad_actual in estante[mejor_pais]:
        x = heuristica(ciudad, ciudad_actual);
        if x<maximo:
            maximo = x
            mejor_ciudad = ciudad_actual
        print(nodo(ciudad_actual, x))
    print(mejor([mejor_pais, mejor_ciudad]))
    maximo = INF
    for nombre_actual in estante[mejor_pais][mejor_ciudad]:
        x = heuristica(nombre, nombre_actual)
        if (x<maximo):
            maximo = x
            mejor_solucion = nombre_actual
        print(nodo(nombre_actual, x))
    solucion = estante[mejor_pais][mejor_ciudad][mejor_solucion]
    print(mejor([mejor_pais, 
        mejor_ciudad, 
        mejor_solucion, 
        solucion]))
    return solucion

contact_map = {
    'Brazil': {
        'Rio de Janeiro': {
            'Pedro Silva': '111111111',
            'Isabella Santos': '222222222',
            'Lucas Oliveira': '333333333',
            'Mariana Costa': '444444444',
            'Gustavo Pereira': '555555555',
            'Sophia Gomes': '666666666',
            'Enzo Rodrigues': '777777777',
            'Laura Almeida': '888888888'
        },
        'Sao Paulo': {
            'Matheus Fernandes': '111111111',
            'Beatriz Lima': '222222222',
            'Gustavo Barbosa': '333333333',
            'Gabriela Souza': '444444444',
            'Rafael Castro': '555555555',
            'Lara Santos': '666666666',
            'Guilherme Carvalho': '777777777',
            'Isabela Ferreira': '888888888'
        }
    },
    'China': {
        'Beijing': {
            'Li Wei': '111111111',
            'Zhang Jing': '222222222',
            'Wang Tao': '333333333',
            'Liu Mei': '444444444',
            'Chen Xue': '555555555',
            'Zhao Ming': '666666666',
            'Huang Xin': '777777777',
            'Xu Yang': '888888888'
        },
        'Shanghai': {
            'Zhou Fang': '111111111',
            'Wu Ying': '222222222',
            'Sun Lei': '333333333',
            'Cheng Wei': '444444444',
            'Xie Lin': '555555555',
            'Qian Yu': '666666666',
            'Guo Xia': '777777777',
            'Lu Chen': '888888888'
        }
    },
    'United Kingdom': {
        'London': {
            'James Smith': '111111111',
            'Olivia Johnson': '222222222',
            'Jack Wilson': '333333333',
            'Amelia Brown': '444444444',
            'Thomas Taylor': '555555555',
            'Emily Davies': '666666666',
            'William Evans': '777777777',
            'Sophia Hughes': '888888888'
        },
        'Manchester': {
            'Harry Johnson': '111111111',
            'Ava Thompson': '222222222',
            'Charlie Roberts': '333333333',
            'Isla Clark': '444444444',
            'George Wilson': '555555555',
            'Poppy Walker': '666666666',
            'Jacob Hall': '777777777',
            'Olivia Green': '888888888'
        }
    },
    'Canada': {
        'Toronto': {
            'John Doe': '123456789',
            'Jane Smith': '987654321',
            'Samantha Wilder': '555555555',
            'Michael Johnson': '111111111',
            'David Brown': '222222222',
            'Emily Davis': '333333333'
        },
        'Vancouver': {
            'William Wilson': '444444444',
            'Olivia Miller': '666666666',
            'Liam Taylor': '777777777',
            'Sophia Anderson': '888888888',
            'Emma Thompson': '999999999',
            'Jacob Davis': '111122223',
            'Ava White': '333355556',
            'Mia Harris': '777788889'
        },
        'Montreal': {
            'Noah Turner': '444488881',
            'Sophie Clark': '222222299',
            'James Martinez': '777733337',
            'Benjamin Rodriguez': '111111333',
            'Ella Green': '555556666',
            'Emily Mitchell': '999994444',
            'Oliver Adams': '888887777',
            'Lucas Lee': '666661111'
        }
    },
    'United States': {
        'New York': {
            'Emma Johnson': '222222222',
            'Lucas Martin': '777777777',
            'Alexander Walker': '333333333',
            'Liam White': '111111111',
            'Olivia Lewis': '888888888',
            'Emily Brown': '999999999',
            'Mason Anderson': '444444444',
            'Sophia Wilson': '555555555'
        },
        'Los Angeles': {
            'Aiden Davis': '111111111',
            'Isabella Garcia': '222222222',
            'Matthew Martinez': '333333333',
            'Sofia Johnson': '444444444',
            'William Thompson': '555555555',
            'Mia Anderson': '666666666',
            'Daniel Wilson': '777777777',
            'Victoria Lewis': '888888888'
        },
        'Chicago': {
            'Joseph Turner': '111111111',
            'Charlotte Clark': '222222222',
            'David Hernandez': '333333333',
            'Elizabeth Davis': '444444444',
            'Michael Thompson': '555555555',
            'Andrew Johnson': '666666666',
            'Sophia Miller': '777777777',
            'Daniel Wilson': '888888888'
        }
    }
}

solucion_avara(contact_map);
#print(solucion_avara(contact_map))
