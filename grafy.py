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
    queue = []
    parent =[-1 for i in range(0,len(G))]
    queue.append(s)
    distances = [1000000 for vertex in range(0,len(G))]
    distances[s] = 0
    vertices = [i for i in range(len(G))]


    for i in range(0,len(G)):
        curr = min_distance(G,visited,distances)
        visited[curr]=1
        print(curr)
        for i in G[curr]:
            wierzcholek, waga = i
            if visited[wierzcholek] == 0:
               if distances[wierzcholek]>distances[curr]+waga:
                   distances[wierzcholek] = distances[curr]+waga
    print(visited)
    print(distances)
    return distances[t]



G = [[(1,1), (2,5)],
[(2,3)],
[]]

print( path_cost( G, 0, 2 ) )



