HashTable = [-1 for i in range(5)]

def get_index(key,size):
    return key%size

def insert(key, hasht):
    index = get_index(key,len(hasht))
    startindex = index
    while hasht[index]!=-1:
        if index == len(hasht) - 1:
            index = 0
        else:
            index+=1
        if startindex==index:
            print("HashTable full")
            return False
    hasht[index] = key
    return True


def doskonalosc(ht):
    betterone = [-1 for i in range(2*len(ht))]

    for i in range(len(ht)):
        if i == get_index(ht[i],len(ht)):
            insert(ht[i],betterone)
            ht[i]=-1
    for i in range(len(ht)):
        if ht[i] is not -1:
            insert(ht[i],betterone)

    return betterone

insert(0,HashTable)
insert(5,HashTable)
insert(1,HashTable)
insert(6,HashTable)
insert(4,HashTable)
print(HashTable)
print(doskonalosc(HashTable))