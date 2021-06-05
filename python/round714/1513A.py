from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    if n % 2 == 0 and k >= n // 2 or n % 2 == 1 and k > n // 2:
        print(-1)
    else:
        a = list(range(1, n + 1))
        res = [-1]*n
        cur = 0
        for i in range(n):
            if i % 2 == 1 and k > 0:
                res[i] = a[-k]
                k-=1
            else:
                res[i] = a[cur]
                cur += 1
        print(*res)
