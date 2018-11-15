import math
import queue
from copy import deepcopy

percorrido = 'o'
parede = 'X'

def euclidean(a, b):
    xa, ya = a
    xb, yb = b
    return math.sqrt( (xb - xa)**2 + (yb - ya)**2 )

def manhattan (a, b):
    xa, ya = a
    xb, yb = b
    return (abs(xb - xa) + abs(yb - ya))

def printmapa (mapa, camefrom, ponto_f):
    mapa_f = deepcopy(mapa)
    altura = len(mapa_f)
    largura = len(mapa_f[0])
    y, x = ponto_f
    
    while (camefrom[y][x] != 'I'):
        mapa_f[y][x] = percorrido
        y,x = camefrom[y][x]
    mapa_f[y][x] = percorrido
    
    for i in range(altura):
        for j in range(largura):
            if mapa_f[i][j] == parede or mapa_f[i][j] == percorrido:
                print('|' + mapa_f[i][j] + '|', end = '')
            else:
                print('| |', end = '')
        print()
    return 0
    
def largura(mapa, inicial, final):
    a = len(mapa)
    l = len(mapa[0])
    y, x = inicial
    nos_exp = 1
    
    mapheu = [[math.inf]*l for i in range (a)]
    mapheu[y][x] = 0
    
    camefrom = [[math.inf]*l for i in range (a)]
    camefrom[y][x] = 'I'
    
    fila = queue.Queue()
    fila.put([y, x])

    while not fila.empty():
        y, x = fila.get()
        if [y, x] == final:
            for i in range(a):
                print(mapheu[i])
            print("Nós expandidos : ", nos_exp, "\n")
            printmapa(mapa, camefrom, final)
            return 0
                
        dist1 = mapheu[y][x]
        
        if (x - 1) >= 0:
            if mapa[y][x-1] != parede:
                if mapheu[y][x-1] > dist1 + 1:
                    mapheu[y][x-1] = dist1 + 1
                    camefrom[y][x-1] = [y,x]
                    fila.put([y, x-1])
                    nos_exp += 1
        if (y - 1) >= 0:
            if mapa[y-1][x] != parede:
                if mapheu[y-1][x] > dist1 + 1:
                    mapheu[y-1][x] = dist1 + 1
                    camefrom[y-1][x] = [y,x]
                    fila.put([y-1, x])
                    nos_exp += 1
        if (x + 1) < l:
            if mapa[y][x+1] != parede:
                if mapheu[y][x+1] > dist1 + 1:
                    mapheu[y][x+1] = dist1 + 1
                    camefrom[y][x+1] = [y,x]
                    fila.put([y, x+1])
                    nos_exp += 1
        if (y + 1) < a:
            if mapa[y+1][x] != parede:
                if mapheu[y+1][x] > dist1 + 1:
                    mapheu[y+1][x] = dist1 + 1
                    camefrom[y+1][x] = [y,x]
                    fila.put([y+1, x])
                    nos_exp += 1
        
    print("Ponto final não encontrado")
    return 1


def dijkstra(mapa, inicial, final):
    a = len(mapa)
    l = len(mapa[0])
    y, x = inicial
    nos_exp = 1
    
    mapheu = [[math.inf]*l for i in range (a)]
    mapheu[y][x] = 0
    
    camefrom = [[math.inf]*l for i in range (a)]
    camefrom[y][x] = 'I'
    
    fila = queue.PriorityQueue()
    prioridade = 0
    fila.put((prioridade, [y, x]))
    flag = [[y,x]]

    while not fila.empty():
        dist1, [y, x] = fila.get()
        
        if [y, x] == final:
            for i in range(a):
                print(mapheu[i])
            print("Nós expandidos : ", nos_exp, "\n")
            printmapa(mapa, camefrom, final)
            return 0
        
        if (x - 1) >= 0:
            if mapa[y][x-1] != parede:
                if [y,x-1] not in flag: 
                    prioridade = dist1 + mapa[y][x-1]
                    mapheu[y][x-1] = prioridade
                    camefrom[y][x-1] = [y,x]
                    fila.put((prioridade, [y, x-1]))
                    flag += [[y, x-1]]
                    nos_exp += 1
        if (y - 1) >= 0:
            if mapa[y-1][x] != parede:
                if [y-1,x] not in flag:
                    prioridade = dist1 + mapa[y-1][x]
                    mapheu[y-1][x] = prioridade
                    camefrom[y-1][x] = [y,x]
                    fila.put((prioridade, [y-1, x]))
                    flag += [[y-1, x]]
                    nos_exp += 1
        if (x + 1) < l:
            if mapa[y][x+1] != parede:
                if [y,x+1] not in flag:
                    prioridade = dist1 + mapa[y][x+1]
                    mapheu[y][x+1] = prioridade
                    camefrom[y][x+1] = [y,x]
                    fila.put((prioridade, [y, x+1]))
                    flag += [[y, x+1]]
                    nos_exp += 1
        if (y + 1) < a:
            if mapa[y+1][x] != parede:
                if [y+1,x] not in flag:
                    prioridade = dist1 + mapa[y+1][x]
                    mapheu[y+1][x] = prioridade
                    camefrom[y+1][x] = [y,x]
                    fila.put((prioridade, [y+1, x]))
                    flag += [[y+1, x]]
                    nos_exp += 1
        
    print("Ponto final não encontrado")
    return 1


def greedy(mapa, inicial, final):
    a = len(mapa)
    l = len(mapa[0])
    y, x = inicial
    nos_exp = 1
    
    mapheu = [[math.inf]*l for i in range (a)]
    mapheu[y][x] = manhattan([x, y], final)
    
    camefrom = [[math.inf]*l for i in range (a)]
    camefrom[y][x] = 'I'
    
    fila = queue.PriorityQueue()
    prioridade = 0
    fila.put((prioridade, [y, x]))
    flag = [[y,x]]

    while not fila.empty():
        dist, [y, x] = fila.get()
        
        if [y, x] == final:
            for i in range(a):
                print(mapheu[i])
            print("Nós expandidos : ", nos_exp, "\n")
            printmapa(mapa, camefrom, final)
            return 0
                
        if (x - 1) >= 0:
            if mapa[y][x-1] != parede:
                if [y,x-1] not in flag: 
                    prioridade = manhattan([x-1, y], final)
                    mapheu[y][x-1] = prioridade
                    camefrom[y][x-1] = [y,x]
                    fila.put((prioridade, [y, x-1]))
                    flag += [[y, x-1]]
                    nos_exp += 1
        if (y - 1) >= 0:
            if mapa[y-1][x] != parede:
                if [y-1,x] not in flag:
                    prioridade = manhattan([x, y-1], final)
                    mapheu[y-1][x] = prioridade
                    camefrom[y-1][x] = [y,x]
                    fila.put((prioridade, [y-1, x]))
                    flag += [[y-1, x]]
                    nos_exp += 1
        if (x + 1) < l:
            if mapa[y][x+1] != parede:
                if [y,x+1] not in flag:
                    prioridade = manhattan([x+1, y], final)
                    mapheu[y][x+1] = prioridade
                    camefrom[y][x+1] = [y,x]
                    fila.put((prioridade, [y, x+1]))
                    flag += [[y, x+1]]
                    nos_exp += 1
        if (y + 1) < a:
            if mapa[y+1][x] != parede:
                if [y+1,x] not in flag:
                    prioridade = manhattan([x+1, y], final)
                    mapheu[y+1][x] = prioridade
                    camefrom[y+1][x] = [y,x]
                    fila.put((prioridade, [y+1, x]))
                    flag += [[y+1, x]]
                    nos_exp += 1
        
    print("Ponto final não encontrado")
    return 1

def AStar(mapa, inicial, final):
    a = len(mapa)
    l = len(mapa[0])
    y, x = inicial
    nos_exp = 1
    
    mapdist = [[math.inf]*l for i in range (a)]
    mapdist[y][x] = 0
    
    mapheu = [[math.inf]*l for i in range (a)]
    
    camefrom = [[math.inf]*l for i in range (a)]
    camefrom[y][x] = 'I'
    
    fila = queue.PriorityQueue()
    prioridade = mapdist[y][x] + manhattan([x, y], final)
    fila.put((prioridade, [y, x]))
    mapheu[y][x] = prioridade
    flag = [[y,x]]

    while not fila.empty():
        dist, [y, x] = fila.get()
        
        if [y, x] == final:
            for i in range(a):
                print(mapheu[i])
            print("Nós expandidos : ", nos_exp, "\n")
            printmapa(mapa, camefrom, final)
            return 0
                
        if (x - 1) >= 0:
            if mapa[y][x-1] != parede:
                if [y,x-1] not in flag:
                    mapdist[y][x-1] = mapdist[y][x] + 1
                    prioridade = mapdist[y][x-1] + manhattan([x-1, y], final)
                    mapheu[y][x-1] = prioridade
                    camefrom[y][x-1] = [y,x]
                    fila.put((prioridade, [y, x-1]))
                    flag += [[y, x-1]]
                    nos_exp += 1
        if (y - 1) >= 0:
            if mapa[y-1][x] != parede:
                if [y-1,x] not in flag:
                    mapdist[y-1][x] = mapdist[y][x] + 1
                    prioridade = mapdist[y-1][x] + manhattan([x, y-1], final)
                    mapheu[y-1][x] = prioridade
                    camefrom[y-1][x] = [y,x]
                    fila.put((prioridade, [y-1, x]))
                    flag += [[y-1, x]]
                    nos_exp += 1
        if (x + 1) < l:
            if mapa[y][x+1] != parede:
                if [y,x+1] not in flag:
                    mapdist[y][x+1] = mapdist[y][x] + 1
                    prioridade = mapdist[y][x+1] + manhattan([x+1, y], final)
                    mapheu[y][x+1] = prioridade
                    camefrom[y][x+1] = [y,x]
                    fila.put((prioridade, [y, x+1]))
                    flag += [[y, x+1]]
                    nos_exp += 1
        if (y + 1) < a:
            if mapa[y+1][x] != parede:
                if [y+1,x] not in flag:
                    mapdist[y+1][x] = mapdist[y][x] + 1
                    prioridade = mapdist[y+1][x] + manhattan([x, y+1], final)
                    mapheu[y+1][x] = prioridade
                    camefrom[y+1][x] = [y,x]
                    fila.put((prioridade, [y+1, x]))
                    flag += [[y+1, x]]
                    nos_exp += 1
        
    print("Ponto final não encontrado")
    return 1

def main():
    mapa = [[ 1 , 1 , 1 , 1 , 1 , 1, 1 ],
            ['X','X','X','X','X', 4, 1 ],
            [ 1 , 1 , 1 ,'X', 1 , 7, 1 ],
            [ 1 , 1 , 1 ,'X', 8 , 1, 1 ],
            [ 1 , 1 , 5 , 1 , 1 , 5, 9 ],
            [ 1 , 1 , 2 , 1 , 1 , 3, 1 ],
            [ 1 , 1 , 1 , 1 , 9 , 1, 1 ]]
    
    inicial = [6, 0]    #[linha, coluna]
    final = [0, 0]      #[linha, coluna]
    
    print("\n----Dijkstra----\n")
    dijkstra(mapa, inicial, final)
    print("\n----Largura----\n")
    largura(mapa, inicial, final)
    print("\n----Greedy----\n")
    greedy(mapa, inicial, final)
    print("\n----A*----\n")
    AStar(mapa, inicial, final)
    return 0
    
main()