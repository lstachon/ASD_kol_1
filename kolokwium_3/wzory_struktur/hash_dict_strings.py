import random

class Node:
    def __init__(self , key = None , value = None):
        self.key = key
        self.val = value
        self.next = None

class Hashtable:
    PRIME = 1118317
    A = random.randint(1, PRIME)
    B = random.randint(1, PRIME)

    def __init__(self , size):
        self.arr = [None] * size

    def hashFun(self , elem):
        res =0
        if type(elem) is str:
            for i in range(len(elem)):
                res+= ord(elem[i])
            res = (self.A * res + self.B) % self.PRIME
            return res % len(self.arr)
        else:
            elem = (self.A * elem + self.B) % self.PRIME
            return elem % len(self.arr)

    def insert(self , key , value):
        newNode = Node(key , value)
        hash = self.hashFun( key )
        newNode.next = self.arr[hash]
        self.arr[hash] = newNode
    def find(self , key):
        hash = self.hashFun( key )
        curr = self.arr[hash]
        while curr != None:
            if curr.key == key:
                return curr.val
            else:
                curr = curr.next
        return None
    def remove(self , key):
        hash = self.hashFun(key)
        if self.arr[hash].key == key:
            self.arr[hash] = self.arr[hash].next
        curr = self.arr[hash]
        while curr != None:
            if curr.key == key:
                before.next = curr.next
                del curr
                return
            else:
                before = curr
                curr = curr.next
def prt(arr):
    for elem in arr:
        if elem == None:
            print(" ," , end="")
        else:
            print(elem.val,"," , end="")

    print()
H = Hashtable(15)
prt(H.arr)
H.insert('aa','aa')
prt(H.arr)
H.insert('bbbbb' , 'bbbbb')
prt(H.arr)
print(H.find('aa'))

prt(H.arr)
# H.insert(98 , 98)
# prt(H.arr)
# H.insert(1234 , 1234)
# prt(H.arr)
# H.insert(7 , 7)
# prt(H.arr)
# print(H.find(3))
# print(H.find(5))
# print(H.find(98))
# print(H.find(1234))
# print(H.find(7))
# H.remove(3)
# prt(H.arr)
# H.remove(1234)
# prt(H.arr)
# H.remove(7)
# prt(H.arr)
# print(H.find(3))
# print(H.find(5))
# print(H.find(98))
# print(H.find(1234))
# print(H.find(7))