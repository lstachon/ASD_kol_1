# kombinacje na stringu
output = []

def kombinacje_wraper(arr, k):
    data = [0 for i in range(0,len(arr))]
    kombinacje(arr, data, 0,len(arr)-1, 0, k)
    return output

def kombinacje(arr, data, start, end, index, k):
    if index == k:
        temp = []
        for j in range(k):
            temp.append(data[j])
        output.append(temp)
        return
    i = start
    while i <= end and end - i + 1 >= k - index:
        data[index] = arr[i]
        kombinacje(arr, data, i + 1,end, index + 1, k)
        i += 1

arr = [1, 2, 3, 4, 5]
r = 3
kombinacje_wraper(arr, r)
print(output)
# print('##################################')
# a = printCombination(arr,r)
# print (a)