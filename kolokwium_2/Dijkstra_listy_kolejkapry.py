#Łukasz Stachoń


def dijkstra( G, s ):
    from queue import PriorityQueue
    q = PryiorityQueue()
    n = len(G)
    distance =[10000 for i in range(0,n)]
    queue = []
    visited = [False for i in range(0,n)]
    parent = [None for i in range(0,n)]
    for i in range(0, n):
        queue.append(i)
    distance[s]=0

    while len(queue)!=0:
        u = q.get()
        queue.remove(u)
        visited[u] = True

        for i in G[u]:
            v, w = i
            alt = distance[u] + w
            if alt < distance[v] and visited[v] == False:
                distance[v] = alt
                parent[v] = u

    return parent


G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]
print( dijkstra( G, 0 ) )
# wypisze [None,0,1,2]