class field:
    def __init__(self,value = None, long=None, short=None):
        self.value =value
        self.long = long
        self.short = short

class tejbl:
    def __init__(self,size):
        self.table = [None for i in range(size)]

    def add_field(self,value,long,short):
        i = 0
        a = field(value,long,short)
        while self.table[i]!= None:
            i+=1
        self.table[i] = a

    def printen(self):
        for i in range(len(self.table)):
            print(self.table[i].value)

def makethisshit(T):
    G = [[] for i in range(2*(len(T)) - 2)]
    index = 0
    for i in range(len(T) - 1):
        G[index] = [i, i + T[i].short,-T[i].value]
        index += 1
        G[index] =[i, i + T[i].long, -T[i].value]
        index += 1
    print(G)
    return G

from sys import maxsize

def BellmanFord(graph, V, E, src):
    dis = [maxsize] * V

    dis[src] = 0

    for i in range(V - 1):
        for j in range(E):
            if dis[graph[j][0]] + \
                    graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2]

    for i in range(E):
        x = graph[i][0]
        y = graph[i][1]
        weight = graph[i][2]
        if dis[x] != maxsize and dis[x] + \
                weight < dis[y]:
            print("Graph contains negative weight cycle")

    print("Vertex Distance from Source")
    for i in range(V):
        print("%d\t\t%d" % (i, -dis[i]))


table = tejbl(3)

table.add_field(1,2,1)
table.add_field(1,1,1)
table.add_field(2,0,0)

table.printen()

G=makethisshit(table.table)

BellmanFord(G,3,len(G),0)