class Node:
    def __init__(self, dest):
        self.val = dest
        self.next= None

class graph:
    def __init__(self,v):
        self.v=v
        self.graph = [None]*self.v

    def add(self,s,d):
        new = Node(d)
        new.next=self.graph[s]
        self.graph[s] = new

    def print_graph(self):
        for i in range(self.v):
            print("wierzcholek",i)
            tmp = self.graph[i]
            while tmp:
                print(tmp.val)
                tmp=tmp.next
            print("\n")


V = 5
g = graph(V)

g.add(0, 1)
g.add(0, 4)
g.add(1, 2)
g.add(1, 3)
g.add(1, 4)
g.add(2, 3)
g.add(3, 4)

g.print_graph()




