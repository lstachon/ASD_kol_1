#bfs dla macierzy sasiedztwa

def BFS(G,s):
    visited = [0 for i in range(len(G))]
    visited[s] = 1
    queue =[]
    queue.append(s)
    r = []
    while len(queue)!= 0:
        a = queue.pop(0)
        print(a," ")
        for i in range(len(G[a])):

            if(G[a][i]==1):
                if visited[i] == 0:
                    queue.append(i)
                    visited[i]=1


