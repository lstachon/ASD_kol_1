class Node:
    def __init__(self, value = -1):
        self.val = value
        self.deleted = False


def hashFun(key,N):
    return key % N

class Hashtable:
    def __init__(self , size):
        self.arr = [Node()] * size

    def insert(self ,value):
        newNode = Node(value)
        hash =hashFun(value,len(self.arr))
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


def gonext(table, i):
    x = table.arr[i].val
    k = i
    i = hashFun(table.arr[i].val ,len(table.arr))
    table.arr[k].val = -1
    while table.arr[i].val is not -1:
        i+=1
        i = i % len(table.arr)
    table.arr[k].val=x
    return i

def nicniedziala(table):
    broken_el=[]
    holes=[]
    psuj = None
    for i in range(len(table.arr)+1):
        i = i % len(table.arr)
        if table.arr[i].val is not -1 and gonext(table, i) is not i:
            broken_el.append(table.arr[i].val)
        if table.arr[i].val is -1:
            psuj = i
        elif table.arr[i].val is not -1 and hashFun(table.arr[i].val, len(table.arr)) == i:
            psuj = None
        elif table.arr[i].val is not -1 and psuj is not None and hashFun(table.arr[i].val , len(table.arr)) != i:
            holes.append(psuj)

    return holes, broken_el

H = Hashtable(15)
H.insert(3)
H.insert(3)
H.insert(4)
H.insert(3)
H.insert(12)
H.insert(12)
H.insert(13)
H.insert(12)
H.insert(12)

# H.arr[14].val=-1
H.arr[5].val=-1

prt(H.arr)

print(nicniedziala(H))