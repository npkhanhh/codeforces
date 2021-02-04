from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    dp = [1] * (n + 1)
    res = 1
    a = [0] + list(map(int, stdin.readline().split()))
    for i in range(1, n+1):
        for j in range(i*2, n+1, i):
            if a[j] > a[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(max(dp))
