from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    for i in range(n-1):
        t = min(a[i], k)
        a[i] -= t
        k -= t
        a[-1] += t
        if k == 0:
            break

    print(*a)
