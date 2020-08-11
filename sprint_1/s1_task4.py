def findPermutation(n, p, q):
    r = []
    for i in range(0,n):
        for j in range(0,n):
            if q[i] == p[j]:
                r.append(j+1)
    return r
