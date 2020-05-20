#algorytm znajdujący sciezke dla malych wag

def BFS(G,s,e):
    visited = [0 for i in range(len(G))]
    visited[s] = 1
    queue =[]
    queue.append(s)
    parent = [0]*len(G)
    distance=[1]*len(G)
    distance[s] = 0
    
    while len(queue)!= 0:
        print('graf:',G)
        a = queue.pop(0)
        distance[a]+=1
        print(a," ")
        for i in range(len(G[a])):
            if(G[a][i]>0):
                if visited[i] == 0:
                    G[a][i]-=1
                    queue.append(i)
                    parent[i] = a
                    if G[a][i]==0:
                        visited[i]=1
                        distance[i] = distance[a]+1
                        parent[i] = a



    return distance,parent




G=[[0 for i in range(4)] for j in range(4)]

G[0][1]=5
G[0][2]=2
G[2][1]=1
G[1][3]=1

print(BFS(G,0,3))
