
def brejkdown(job,i,j):
    res = 0
    if job[j][0]>job[j-1][1]:
        res = job[j][0] - job[j-1][1]
        print(res)
        return res
    else:
        return False


def min_time(job,k):
    f = [[99999 for i in range(len(job))]for i in range(len(job))]

    for i in range(len(job)):
        f[0][i] = 0

    for i in range(1,len(job)):
        for j in range(len(job)):
            if i >  j:
                f[i][j]=99999
            brejk = brejkdown(job,i, j)
            if brejk is False:
                f[i][j]=99999
            else:
                f[i][j] = min(f[i][j-1],f[i-1][j-1]) + brejk
    print(f)

job = [(0,2),(3,4),(3.5,6),(7,8)]

min_time(job,3)