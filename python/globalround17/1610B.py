from sys import stdin

for zz in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    c = []
    l = 0
    r = n-1
    while l < r:
        if a[l] != a[r]:
            c.append(a[l])
            c.append(a[r])
            break
        l += 1
        r -= 1
    res = 'YES'
    for i in c:
        res = 'YES'
        l = 0
        r = n-1
        while l < r:
            if a[l] == i:
                l += 1
                continue
            if a[r] == i:
                r -= 1
                continue
            if a[l] != a[r]:
                res = 'NO'
                break
            l += 1
            r -= 1
        if res == 'YES':
            break
    print(res)


