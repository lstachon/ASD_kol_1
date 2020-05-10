#algorytm znajdujący sciezke dla malych wag

def BFS(G,s,e):
    visited = [0 for i in range(len(G))]
    visited[s] = 1
    queue =[]
    queue.append(s)
    result =[]
    while len(queue)!= 0:
        a = queue.pop(0)
        print(a," ")
        if(a==e):
            return 0

        for i in range(len(G[a])):

            if(G[a][i]>0):
                if visited[i] == 0:
                    queue.append(i)
                    G[a][i]-=1
                    if(G[a][i]==0):
                        visited[i]=1




G=[[0 for i in range(4)] for j in range(4)]

G[0][1]=5
G[0][2]=2
G[2][1]=1
G[1][3]=1

BFS(G,0,3)