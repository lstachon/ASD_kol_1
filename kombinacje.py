# kombinacje na stringu
def printCombination(arr, r):
    data = [0 for i in range(0,len(arr))]

    kombinacje(arr, data, 0,len(arr)-1, 0, r)

def kombinacje(arr, data, start, end, index, r):
    if (index == r):
        for j in range(r):
            print(data[j], end=" ")
        print()
        return
    i = start
    while (i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        kombinacje(arr, data, i + 1,end, index + 1, r)
        i += 1

arr = [1, 2, 3, 4, 5]
r = 3
printCombination(arr, r)