#counting sort na stringach

def coutningsort(arr):
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]

    # ans = ["" for _ in arr]
    for i in arr:
        count[ord(i)] += 1

    for i in range(len(count)):
        count[i] += count[i-1]
    print(count)
    for i in range(0,len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    ans = ["" for i in range(len(arr))]

    for i in range(len(arr)):
        ans[i] = output[i]

    return ans


a = "cba"

ans=coutningsort(a)

print(ans)