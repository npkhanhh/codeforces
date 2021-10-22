from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = sum(a)
    avg = s/n
    tot = s-avg*(n-2)
    if tot % 1 > 10**-8:
        print(0)
        continue
    tot = int(tot)
    d = {}
    res = 0
    for i in a:
        if tot - i in d:
            res += d[tot-i]

        if i not in d:
            d[i] = 1
        else:
            d[i]+= 1
    print(res)

