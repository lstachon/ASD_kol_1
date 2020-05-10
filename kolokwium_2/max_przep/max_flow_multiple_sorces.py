def BFS(G,s,e,parent):
    queue=[]
    visited = [0 for i in range(0,len(G))]
    visited[s]=1
    queue.append(s)

    while len(queue)!=0:
        a=queue.pop(0)
        if a == e:
            return True
        for i in range(0,len(G)):
            if G[a][i]>0:
                if visited[i]==0:
                    visited[i]=1
                    queue.append(i)
                    parent[i]=a

    return False

def max_flow( c, s, t):
    res_g=[[0 for i in range(len(c)+2)]for j in range(len(c)+2)]
    for i in range(0,len(c)):
        for j in range(0,len(c)):
            res_g[i][j]=c[i][j]
    parent=[-1 for i in range(0,len(res_g))]
    mflow=0
    supersorce=len(c)
    supersink=len(c)+1
    for i in range(0,len(s)):
        res_g[supersorce][s[i]]=9999
    for i in range(0,len(t)):
        res_g[t[i]][supersink]=9999

    while BFS(res_g,supersorce,supersink,parent):
        a = supersink
        path=[]
        path.append(a)
        while a is not supersorce:
            a = parent[a]
            path.append(a)
        print(path)

        min=99999
        for i in range(0,len(path)-1):

            if res_g[path[i+1]][path[i]]<min:
                min=res_g[path[i+1]][path[i]]

        for i in range(0, len(path) - 1):
            res_g[path[i]][path[i+1]]=min
            res_g[path[i+1]][path[i]]-=min

        mflow+=min

    return mflow


G=[[0 for i in range(8)] for j in range(8)]
G[0][4]=1
G[1][4]=2
G[1][5]=3
G[2][5]=4
G[3][5]=5
G[3][7]=6
G[4][6]=2
G[5][6]=3
G[5][7]=1
s=[0,1,2,3]
t=[6,7]
print(max_flow(G,s,t))

