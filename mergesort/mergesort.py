def srodeczek(A, i, j):
    a = len(A) / 2
    a = int(a)
    return a


def merge(A, B):
    a = 0
    b = 0
    stefan = []
    if (A == None or len(A) == 0):
        return B
    if (B == None or len(B) == 0):
        return A
    while a != len(A) and b != len(B):
        if A[a] <= B[b]:
            stefan.append(A[a])
            a += 1
        else:
            stefan.append(B[b])
            b += 1
    while a != len(A):
        stefan.append(A[a])
        a += 1
    while b != len(B):
        stefan.append(B[b])
        b += 1
    return stefan


def mergesort(A, poczatke, konie):
    if (len(A) > 1):
        mid = srodeczek(A, poczatke, konie)
        lewuncio = mergesort(A[:mid], poczatke, mid)
        pawica = mergesort(A[mid:], mid + 1, konie)

        resultaten = merge(lewuncio, pawica)
        return resultaten
    return A


def sumbetween(A, form, to):
    sum = 0
    for i in range(form, to + 1):
        sum += A[i]
    return sum

    # dopoki nie ma pojedycznych elementow
    # wyznaczam srodek mid
    # tab prawa  = mergeort(a , midzio , koniec)
    # res =  merge(tabl_lewa, tablia_pra)

    # tab lewa = mergesort( a , poczat , midzio)
    # a potem lacze w chuj te wszystkie maluskie tablicuncie


# A = [3,1,2,6,7,34,67]
# A = mergesort(A,0,len(A)-1)
# print(A)
# a = sumbetween(A,1,3)
# print(a)

A = [5][5]

for i in range(0, 5):
    A
