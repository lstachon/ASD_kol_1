# countingsort

def countingsort(arr):
    min = 100000000
    max = -10000000
    for i in range(0,len(arr)):
        if arr[i]<min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    a = max - min
    T = [0 for i in range(0,a+1)]

    for j in range(0,len(arr)):
        T[arr[j]-min]+=1

    for i in range(1,len(T)):
        T[i]+=T[i-1]

    res =[0 for i in range(0,len(arr))]

    for i in range(0,len(arr)):
        res[T[arr[i]-min]-1] = arr[i]
        T[arr[i]-min] -=1

    return res


arr = [600,605,601,601,605,606]

print(countingsort(arr))



