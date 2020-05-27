from sys import stdin

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, stdin.readline().split()))
    b = sorted(map(int, stdin.readline().split()), reverse=True)
    t = k
    for i in range(k):
        if a[i] >= b[i]:
            t = i
            break
    print(sum(b[:t]) + sum(a[t:]))

