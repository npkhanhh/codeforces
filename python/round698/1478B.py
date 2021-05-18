from sys import stdin

for _ in range(int(stdin.readline())):
    n, d = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    for i in a:
        if i >= d*10 or i % d == 0:
            print('YES')
            continue
        res = 'NO'
        while i > 10:
            if i % 10 == d:
                res = 'YES'
                break
            i -= d
        print(res)
