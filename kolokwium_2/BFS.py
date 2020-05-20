#bfs dla macierzy sasiedztwa

def BFS(G,s,e):
    visited = [0 for i in range(len(G))]
    visited[s] = 1
    queue =[]
    queue.append(s)
    parent = [None]*len(G)
    distance=[None]*len(G)
    distance[s] = 0

    while len(queue)!= 0:
        a = queue.pop(0)
        print(a," ")
        for i in range(len(G[a])):
            if(G[a][i]>0):
                if visited[i] == 0:
                    queue.append(i)
                    visited[i]=1
                    parent[i]=a
                    distance[i] = distance[a]+1
                    parent[i] = a



    return distance,parent



G=[[0 for i in range(4)] for j in range(4)]

G[0][1]=1
G[0][2]=1
G[2][1]=1
G[1][3]=1

print(BFS(G,0,3))