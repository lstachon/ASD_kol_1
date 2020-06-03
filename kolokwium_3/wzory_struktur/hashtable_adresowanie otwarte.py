class element:
    def __init__(self, value = None):
        self.value = value
        self.deleted = 1
        self.empty = 1

import random

class Hashtable:
    PRIME = 1118317
    A = random.randint(1, PRIME)
    B = random.randint(1, PRIME)

    def __init__(self , size):
        self.arr = [None] * size

    def hashFun(self , elem):
        elem = (self.A*elem + self.B) % self.PRIME
        return elem % len(self.arr)

    def insert(self , value):
        newelement = element(value)
        hash = self.hashFun(value)
        self.arr[hash] = newelement

    def find(self , key):
        hash = self.hashFun( key )
        curr = self.arr[hash]
        while curr != None:
            if curr.key == key:
                return curr.val
            else:
                curr = curr.next
        return None


def prt(arr):
    for elem in arr:
        if elem == None:
            print(" ," , end="")
        else:
            print(elem.value,"," , end="")

    print()


H = Hashtable(15)
prt(H.arr)
H.insert(3)
prt(H.arr)
H.insert(5)
prt(H.arr)
H.insert(98 )
prt(H.arr)
H.insert(1234)
prt(H.arr)
H.insert(7 )
prt(H.arr)