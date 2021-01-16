from sys import stdin


for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
    if len(d) > k:
        print(-1)
    else:
        z = 1
        while len(d) < k:
            if z not in d:
                d[z] = 1
            z += 1
        res = list(d.keys())*n
        print(len(res))
        print(*res)
