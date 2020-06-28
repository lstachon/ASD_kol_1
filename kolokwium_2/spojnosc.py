
def DFS(G,s):
    visited =[0 for i in range(len(G))]

    licznik = 0

    stack = []

    stack.append(s)
    visited[s]=1
    while len(stack)!=0:
        a = stack.pop()
        print(a)
        licznik += 1
        for i in range(len(G)):
            if G[a][i] is 1:
                if visited[i] == 0:
                    stack.append(i)
                    visited[i]=1

    if len(G) == licznik:
        return True
    else:
        return False


G = [[0,1,0],[1,0,0],[0,0,0]]


print(DFS(G,0))