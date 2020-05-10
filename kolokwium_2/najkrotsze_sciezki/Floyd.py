#Łukasz Stachoń
#algorytm ma złożoność n^3
#niewaidomo czy graf jest gęsty i dlatego algorytm floyd-warshalla ma tu sens
#złożoność n^3


# w poleceniu nie jest powiedziane czy pojawiają sie cykle i czy w takim wypadku w macierzy sąsiedztwa mamy zaznaczyć ze istnieje scieżka z punktu do tego samego punktu więc zakładam że cykle nie istnieją i algorytm ten nie przewiduje cyklów

def tclosure(g):
    n = len(g)
    max_int = 1000000
    for i in range(n):
        for j in range(n):
            if g[i][j] == True:
                g[i][j] = 1
            elif i == j:
                g[i][j] = 0
            else:
                g[i][j] = max_int
    for t in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                g[i][j] = min(g[i][j], g[i][t] + g[t][j])
    for i in range(n):
        for j in range(n):
            if g[i][j] > 0 and g[i][j] != max_int:
                g[i][j] = True
            else:
                g[i][j] = False
    return g

G = [ [False, True , False],
[False, False, True ],
[False, False, False] ]
print( tclosure( G ) ) # wypisze
# [[False, True , True],
# [False, False, True],
# [False, False, False]]
