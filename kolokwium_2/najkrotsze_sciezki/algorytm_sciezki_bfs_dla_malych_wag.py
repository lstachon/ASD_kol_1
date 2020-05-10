#algorytm znajdujący sciezke dla malych wag

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



G=[[0 for i in range(4)] for j in range(4)]

G[0][1]=1
G[0][2]=1
G[1][2]=1
G[2][0]=1
G[2][3]=1
G[3][3]=1

BFS(G,2)