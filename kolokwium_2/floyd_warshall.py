class vertex:
    def __init__(self,shop=False,t=[],edgez=[]):
        self.shop = shop
        self.distance = t
        self.edges = edgez
        self.d_store = 999999

class vertextable:
    def __init__(self,size):
        self.table = [None for i in range(size)]
        self.curwa = 0

    def add(self,shop,t,edgez):
        self.table[self.curwa] = vertex(shop,t,edgez)
        self.curwa += 1

    def printer(self):
        i = 0
        while i is not self.curwa:
            print(i,self.table[i].edges," ")
            i+=1

def floydWarshall(graph):
    dist = [[99999 for i in range(len(graph.table))]for j in range(len(graph.table))]
    for i in range(len(graph.table)):
        for j in range(len(graph.table[i].edges)):
            dist[i][graph.table[i].edges[j]] = graph.table[i].distance[j]

    print("------------------")

    for k in range(len(graph.table)):
        for i in range(len(graph.table)):
            for j in range(len(graph.table)):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )

    for i in range(len(dist)):
        if graph.table[i].shop is False:
            minimum = 9999
            for j in range(len(dist)):
                if graph.table[j].shop is True:
                    if dist[i][j] < minimum:
                        minimum = dist[i][j]
            print(i,minimum)

    printSolution(dist,graph)


def printSolution(dist,graph):
    for i in range(len(graph.table)):
        for j in range(len(graph.table)):
            # if dist[i][j]!=99999:
            print(dist[i][j]
                  , end=" ")
        print()




table = vertextable(4)
table.add(True,[],[])
table.add(False,[5,2,6],[0,3,2])
table.add(True,[],[])
table.add(False,[4,1],[0,2])

table.printer()
floydWarshall(table)