import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


MOD = 998244353
n, m, k = list(map(int, input().split()))
res = pow(m - 1, k, MOD)
res = (res * m) % MOD
res = res * nCr(n - 1, k) % MOD
print(res)
