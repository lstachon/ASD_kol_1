HashTable = [None for i in range(10000)]

def get_index(key):
    return key%len(HashTable)

def find(key):
    index = get_index(key)
    startindex = index
    while HashTable[index]!=key and HashTable[index]!=None:
        if index == len(HashTable) - 1:
            index = 0
        else:
            index+=1
        if startindex==index:
            return ("HashTable full")
    if HashTable[index] == key:
        return key
    else:
        return ("does not exist")


def insert(key):
    index = get_index(key)
    startindex = index
    while HashTable[index]!=None:
        if index == len(HashTable) - 1:
            index = 0
        else:
            index+=1
        if startindex==index:
            print("HashTable full")
            return False
    HashTable[index] = key
    return True


