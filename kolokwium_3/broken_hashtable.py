
class Node:
    def __init__(self, value = -1):
        self.val = value
        self.deleted = False

def hashFun(key,N):
    return key % N

class Hashtable:
    def __init__(self , size):
        self.arr = [Node()] * size

    def insert(self , value):
        newNode = Node(value)
        hash = hashFun(value ,len(self.arr))
        while self.arr[hash].val is not -1 or self.arr[hash].deleted:
            hash+=1
            hash = hash % len(self.arr)
        self.arr[hash] = newNode

def prt(arr):
    for elem in arr:
        if elem == None:
            print(" ," , end="")
        else:
            print(elem.val,"," , end="")
    print()






H = Hashtable(15)
H.insert(3)
H.insert(5)
H.insert(3)
H.insert(12)
H.insert(12)
H.insert(13)
H.insert(12)
H.insert(12)
H.arr[14].val=-1
prt(H.arr)