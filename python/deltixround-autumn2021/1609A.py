from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    t = 0
    origin = sum(a)
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            t += 1
    m = max(a)
    idx = a.index(m)
    a[idx]*= pow(2, t)
    print(max(origin, sum(a)))

