from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = sorted(a)
    m = min(a)
    highest = -1
    res = 'YES'
    for i in range(n):
        if a[i] != b[i] and a[i] % m != 0:
            res = 'NO'
            break
    print(res)



