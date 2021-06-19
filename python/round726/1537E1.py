import math




n, k = list(map(int, input().split()))
s = input().strip()
res = 'z' * k
for i in range(1, n+1):
    a, b = divmod(k, i)
    offset = 1 if b > 0 else 0
    s_t = s[:i] * (a + offset)
    if s_t[:k] < res:
        res = s_t[:k]

print(res)
