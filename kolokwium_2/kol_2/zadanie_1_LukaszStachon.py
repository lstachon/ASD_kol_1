#Łukasz Stachoń


class Node:
    def __init__(self):
        self.children =0
        self.child=[]
        self.weight =  0
        self.parents =[]
        self.parent = 0


    def f1(self, node):
        for (a, b) in range(node.child):
            a.weight  = node.weight + b
            a.parent = node
            a.parents += node
            self.f1(a)


    def heavy_path(self,T):
        print(self.f1(T))


A = Node()
B = Node()
C = Node()
A.children =2
A.child = [(B,5,(C,-1))]

