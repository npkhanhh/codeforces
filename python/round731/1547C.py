from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    k, n, m = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    a.append(1000)
    b.append(1000)
    i = 0
    j = 0
    res = []
    while i < n or j < m:
        if a[i] < b[j]:
            if a[i] == 0:
                k += 1
            elif a[i] > k:
                res = -1
                break
            res.append(a[i])
            i += 1
        else:
            if b[j] == 0:
                k += 1
            elif b[j] > k:
                res = -1
                break
            res.append(b[j])
            j += 1

    if res == -1:
        print(res)
    else:
        print(*res)
