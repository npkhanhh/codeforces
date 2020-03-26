n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ak = [0] * k
s = 0
for idx, value in enumerate(a):
    if n - value < k:
        s += value
        ak[n - value] = idx + 1
ak = sorted(ak)
res = 1
for i in range(1, len(ak)):
    res = ((ak[i] - ak[i - 1]) * res) % 998244353
print(s, res)
