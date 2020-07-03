def indukowanie(G,k,G1):
    todel=[]
    for i in range(len(G)):
        l = 0
        for j in range(len(G)):
            if G1[i]:
                if G[i][j] == 1:
                    l+=1
        if G1[i] and l<k:
            todel.append(i)
    if len(todel) == 0:
        return G1
    for i in range(len(todel)):
        G1[todel[i]]=False
        for o in range(len(G)):
            G[todel[i]][o]=0
            G[o][todel[i]]=0
        indukowanie(G,k,G1)

    return G,G1

G=[[0,1,0,0,1,1],
   [1,0,1,0,1,1],
   [0,1,0,1,1,0],
   [0,0,1,0,1,0],
   [1,1,1,1,0,1],
   [1,1,0,0,1,0]]

G1=[True for i in range(len(G))]

def revolution(G,G1):
    size = 0
    for i in range(len(G1)):
        if G1[i]:
            size+=1
    G2 =[[0 for i in range(size)] for j in range(size)]
    k =0
    l = 0
    for i in range(len(G)):
        for j in range(len(G)):
            if G1[i] is True and G1[j] is True:
                G2[k][l]=G[i][j]
                l+=1
        if G1[i]:
            k+=1
    print(G2)






