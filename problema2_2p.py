import sys; 
INF = sys.maxsize

limite = 4
coste = INF
ruta = []

def nt(n): 
    return (1<<n)-1-n

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, x, y):
        s = (heuristica(x, y), x)
        self.insert_helper(s)

    def insert_helper(self, x):
        i = 0
        f = len(self.queue)-1
        r = f+1
        while i<=f: 
            mid = (i+f)>>1
            if self.queue[mid][0] > x[0]:
                r = mid
                f = mid-1
            else: 
                i = mid+1
        self.queue.insert(r, x)

    def pop(self): 
	    return self.queue.pop(0)
	
    def empty(self):
	    return len(self.queue)==0

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
    st = '*'*20
    st +='\n'
    st += 'Ruta de minimo coste seleccionada: \n'
    for a in s:
        st+=a+'\n'
    return st
    
def simulated_annealing(mapa, ruta_actual):
    pila = PriorityQueue()
    aux = nombre
    if len(ruta_actual)==0: 
        aux = pais
    elif len(ruta_actual)==1: 
        aux = ciudad
    for x in mapa: 
        pila.insert(x, aux)
        print(nodo(x, heuristica(x, aux)))
    while not (pila.empty()):
        x = pila.pop()
        if aux is nombre:
            global ruta
            global coste
            global limite
            res = heuristica(aux, x[1])
            for p in ruta_actual: 
                res+=p[0]
            if res < coste: 
                ruta = [x[1] for x in ruta_actual]
                ruta.append(x[1])
                ruta.append(mapa[x[1]])
                coste = res
                print('nueva solucion:')
                print(ruta)
                print('Coste:'+str(coste))
                if (coste<=limite):
                    return ruta
        else:
            antigua_ruta = ruta_actual.copy()
            ruta_actual.append(x)
            print(mejor([x[1] for x in ruta_actual]))
            nueva = simulated_annealing(mapa[x[1]], ruta_actual)
            if len(nueva)>2: 
                return nueva
            ruta_actual = antigua_ruta
    return ruta_actual



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
        },
        'Edinburgh': {
            'Jack Roberts': '111133333',
            'Sophie Martin': '333344444',
            'Oliver White': '555566666',
            'Emily Green': '777799999',
            'Ethan Thompson': '999911111',
            'Olivia Wilson': '222222233',
            'William Harris': '444444455',
            'Charlotte Turner': '666666677',
            'Jacob Thompson': '888888899'
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
    }, 
    'Australia': {
        'Sydney': {
            'Thomas Harris': '111122222',
            'Sophia Miller': '333344444',
            'Jacob Thompson': '555566666',
            'Emily Johnson': '777788888',
            'Olivia Lee': '999911111',
            'Oliver Wilson': '222233333',
            'Charlotte Evans': '444455555',
            'Sophia Anderson': '666677777',
            'Noah Turner': '888899999'
        },
        'Melbourne': {
            'Ella Martinez': '111133333',
            'Noah Turner': '333344444',
            'Olivia Martin': '555566666',
            'William Harris': '777799999',
            'Charlotte Turner': '999911111',
            'Sophia Anderson': '222222233',
            'Matthew Taylor': '444444455',
            'Sarah Wilson': '666666677',
            'Daniel Brown': '888888899'
        },
        'Brisbane': {
            'Sophia Anderson': '111122222',
            'Matthew Taylor': '333344444',
            'Sarah Wilson': '555566666',
            'Daniel Brown': '777788888',
            'Olivia Lee': '999911111',
            'Sophie Harris': '222233333',
            'William Thompson': '444455555',
            'Ava Davis': '666677777',
            'Emma Anderson': '888899999'
        }
    },
    'France': {
        'Paris': {
            'Louis Rousseau': '111133333',
            'Léa Dubois': '333344444',
            'Lucas Martin': '555566666',
            'Chloé Dupont': '777799999',
            'Hugo Leroy': '999911111',
            'Sophia Anderson': '222222233',
            'Jacob Thompson': '444444455',
            'Olivia Wilson': '666666677',
            'Emily Johnson': '888888899'
        },
        'Marseille': {
            'Manon Lambert': '111122222',
            'Emma Petit': '333344444',
            'Maxime Laurent': '555566666',
            'Alice Gauthier': '777788888',
            'Léa Dubois': '999911111',
            'Oliver Wilson': '222233333',
            'Charlotte Evans': '444455555',
            'Sophia Miller': '666677777',
            'Jacob Thompson': '888899999'
        },
        'Lyon': {
            'Sophia Miller': '111133333',
            'Lucas Martin': '333344444',
            'Léa Dubois': '555566666',
            'Louis Rousseau': '777799999',
            'Chloé Dupont': '999911111',
            'Olivia Wilson': '222222233',
            'Jacob Thompson': '444444455',
            'Sophia Anderson': '666666677',
            'Emily Johnson': '888888899'
        }
    }, 
        'Canda': {
        'Toronto': {
            'Jahn Smith': '111111111',  
            'Emily Jhonson': '222222222',  
            'Mikael Davis': '333333333',
            'Sophia Millar': '444444444',  
            'Jakob Thompson': '555555555',
            'Olivia Vilson': '666666666',  
            'Ethan Haris': '777777777',  
            'Isabela Terner': '888888888',  
            'Liam Andarsen': '999999999'  
        },
        'Vancouver': {
            'Sara Wilson': '111122222',  
            'Dani Brown': '333344444',  
            'Olivia Li': '555566666',  
            'Noa Turner': '777788888',  
            'Olivar Martin': '999911111',  
            'Sophi Haris': '222233333', 
            'Wilam Thompson': '444455555',
            'Ava Davs': '666677777',  
            'Ema Anderson': '888899999'  
        },
        'Montreal': {
            'Sofia Anderson': '111133333',  
            'Mathew Taylor': '333344444',  
            'El Martinez': '555566666',  
            'Chlo Vilson': '777799999',  
            'Jams Thompson': '999911111',
            'Grac Terner': '222222233', 
            'Henri Davs': '444444455',  
            'Ma Johnson': '666666677',  
            'Alexandr Smith': '888888899'  
        }
    }
}
#solucion_avara(contact_map)
s = simulated_annealing(contact_map, [])
print(s)
