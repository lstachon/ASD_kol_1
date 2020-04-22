
def path_cost(G,s,t):
    visited=[0 for i in range(0,len(G))]
    queue = []
    parent =[-1 for i in range(0,len(G))]
    visited[s]= 1
    queue.append(s)
    distances = {vertex: 1000000 for vertex in len(G)}
    distances[s] = 0
    vertices = [i for i in range(len(G))]

    while vertices:
        current_vertex = 

        if a == t:
            return path(G,parent,a)

        for i in G[a]:

            wierzcholek, waga = i
            if visited[wierzcholek] == 0:
                queue.append(wierzcholek)
                parent[wierzcholek] = a
                visited[wierzcholek] = 1


def path(G,parent, dest):
    cost = 0
    if parent[dest] == -1:
        if dest < len(G):
            print("v : " + str(dest))
            return 0
    a = path(G,parent,parent[dest])
    print("a: " + str(a))
    cost +=a

    if dest <len(G):
        print(dest)

    return cost


G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]
print( path_cost( G, 0, 3 ) )



