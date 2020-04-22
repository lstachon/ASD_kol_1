def min_distance(G,visited,distances):
    min = 10000000000
    for i in range(0,len(G)):
        if visited[i] == 0:
            if distances[i]<min:
                min = distances[i]
                indeks = i
    return indeks

def path_cost(G,s,t):
    visited=[0 for i in range(0,len(G))]
    distances = [1000000 for vertex in range(0,len(G))]
    distances[s] = 0
    for i in range(0,len(G)):
        curr = min_distance(G,visited,distances)
        visited[curr]=1
        for i in G[curr]:
            wierzcholek, waga = i
            if visited[wierzcholek] == 0:
               if distances[wierzcholek]>distances[curr]+waga:
                   distances[wierzcholek] = distances[curr]+waga
    return distances[t]



G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]
print( path_cost( G, 0, 3 ) )