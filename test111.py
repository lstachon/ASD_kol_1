#Michał Stencel
#dal każdeej liczby zliczamy wystąpienia cyfr jednokrotnych i wielokrotynych
#nastepnie sortujemy countsortem wzgledem wystapien wielokrotnych nastepnie jednokrotnych
#zlozlonosc O(n)
def pretty( number ):
    D = [0] * 10
    while number > 0:
        D[number % 10] += 1
        number = number // 10
    j = 0
    w = 0
    for i in range(10):
        if D[i] == 1:
            j += 1
        elif D[i] > 1:
            w += 1
    return j , w
def countSort(A , j ):
    B = [None] * len(A)
    C = [0] * 10
    for num in A:
        print(num)
        C[num[j]] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        C[A[i][j]] -= 1
        B[C[A[i][j]]] = A[i]
    i = 0
    j = len(A)-1
    while i < j:
        B[i] , B[j] = B[j] , B[i]
        i +=1
        j -=1
    for i in range(len(A)):
        A[i] = B[i]
    print(B)
    print(C)
def pretty_sort( arr ):
    n = len(arr)
    for i in range(n):
        j , w = pretty(arr[i])
        arr[i] = (arr[i] , j , w)
    countSort(arr , 2 )
    print(arr)
    countSort(arr , 1 )
    print(arr)
    for i in range(n):
        arr[i] = arr[i][0]
arr = [123 , 455555 , 1266 , 114577 , 2344 , 67333]
#print(arr)
pretty_sort(arr)
# print(arr)