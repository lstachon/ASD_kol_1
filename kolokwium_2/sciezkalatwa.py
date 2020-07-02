G = [[(1,2), (4, 3)],
[(0, 5)],
[(1, 6)],
[(1,7),(4,4), (0, 5)],
[(0,3),(1, 9)]]

print(G)

print('---------------------------------------------------------------------')

def kamikadze(G):
    destructor2000 =[ 0 for i in range(len(G))]
    for i in range(len(G)):
        if len(G[i])>2:
            destructor2000[i] = 1


    res=floydWarshall(G,destructor2000)
    max=-11111
    for i in range(len(res)):
        for j in range(len(res)):
            if res[i][j] > max and res[i][j]!=99999:
                max=res[i][j]

    return max

def floydWarshall(graph,destructor):
    dist = [[99999 for i in range(len(graph))]for j in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if destructor[i] != 1 and destructor[graph[i][j][0]] != 1:
                dist[i][graph[i][j][0]] = -graph[i][j][1]
    print(dist)

    # for u in range(len(dist)):
    #     for i in range(len(dist[u])):
    #             v,w = a
    #             if dist[u] != float("Inf") and dist[u] + w < dist[v]:
    #                 print("Graph contains negative weight cycle")
    #                 return

    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if i != j and i != k and j != k and dist[i][k] != 99999 and dist[k][j] != 99999:
                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j])
    for i in range(len(dist)):
        for j in range(len(dist)):
            if dist[i][j]!=99999:
                dist[i][j]=-dist[i][j]


    print(dist)
    return dist


def printSolution(dist):
    for i in range(len(dist)):
        for j in range(len(dist)):
            if dist[i][j]!= 99999:
                print(-dist[i][j]
                      , end=" ")
            else:
                print('X'
                      , end=" ")
        print()


def BellmanFord(self, src):
    # Step 1: Initialize distances from src to all other vertices
    # as INFINITE
    dist = [float("Inf")] * self.V
    dist[src] = 0

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for _ in range(self.V - 1):
        # Update dist value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are still in
        # queue
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

                # Step 3: check for negative-weight cycles. The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path, then there
    # is a cycle.



    # print all distance
    self.printArr(dist)

print(kamikadze(G))
