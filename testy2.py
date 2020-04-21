# countingsort

def countingsort(arr):
    min = 100000000
    max = -10000000
    for i in range(0,len(arr)):
        if arr[i]<min:
            min = arr [i]
        if arr[i] > max:
            max = arr[i]
    a = max - min
    T = []
    for i in range(0,a):
        T[i]=0
    for i in range(0,len(arr)):
        T[arr[i]-min]+=1


    for i in range(1,len(arr)):
        T[i]+=T[i-1]

    res =[]

    for i in range(0,T[len(T)-1]):
        


