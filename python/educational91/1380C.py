from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()), reverse=True)
    dp = [0] * n
    res = 0
    for idx, val in enumerate(a):
        needed = math.ceil(x / val) - 1
        if needed == 0:
            dp[idx] = res + 1
            res += 1
        else:
            t = idx - needed - 1
            if t < -1:
                dp[idx] = res
            elif t == -1:
                if res == 0:
                    res = 1
                dp[idx] = res
            else:
                dp[idx] = dp[t] + 1
                if dp[idx] > res:
                    res += 1
    print(res)
