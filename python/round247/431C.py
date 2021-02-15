MOD = 10 ** 9 + 7
def calculate(n, max_k):
    if max_k == 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        m = min(i-1, max_k)
        if i <= max_k:
            dp[i] += 1
        for j in range(1, m + 1):
            dp[i] += dp[i-j]
            dp[i] = dp[i] % MOD
    return dp[-1]


n, k, d = list(map(int, input().split()))
if d > n:
    print(0)
elif d == n:
    print(1)
else:
    total = calculate(n, k)
    no_d = calculate(n, d-1)
    total -= no_d
    if total < 0:
        total += MOD
    print(total)
