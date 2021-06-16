from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    res = min(n, k // 2)
    a = list(range(k // 2 + k % 2, k))

    res += max(0, n - k)
    if n > k:
        a += list(range(k + 1, n + 1))
    print(res)
    print(*a)
