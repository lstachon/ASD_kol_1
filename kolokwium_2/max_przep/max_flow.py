#Łukasz Stachoń

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

def max_flow( c, s, t ):
    res_g=[[0 for i in range(len(c))]for j in range(len(c))]
    for i in range(0,len(c)):
        for j in range(0,len(c)):
            res_g[i][j]=c[i][j]
    parent=[-1 for i in range(0,len(c))]
    mflow=0

    while BFS(res_g,s,t,parent):
        a = t
        path=[]
        path.append(a)
        while a is not s:
            a =parent[a]
            path.append(a)
        min=99999
        for i in range(0,len(path)-1):

            if res_g[path[i+1]][path[i]]<min:
                min=res_g[path[i+1]][path[i]]

        for i in range(0, len(path) - 1):
            res_g[path[i]][path[i+1]]=min
            res_g[path[i+1]][path[i]]-=min

        mflow+=min

    return mflow




c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
print( max_flow( c, 0, 3 ) ) # wypisze 3

#przyklad z wykladu:
# c = [[0 for j in range(6)] for i in range(6)]
# c[0][1]=4
# c[0][4]=3
# c[1][2]=2
# c[4][2]=2
# c[4][5]=2
# c[2][3]=4
# c[5][3]=5
#
# print( max_flow( c, 0, 3 ) ) # wypisze 5
