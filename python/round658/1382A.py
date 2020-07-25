from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    d_a = {}
    for i in a:
        d_a[i] = 1
    res = 'NO'
    tt = 0
    for i in b:
        if i in d_a:
            res = 'YES'
            tt = (1, i)
    print(res)
    if res == 'YES':
        print(*tt)



