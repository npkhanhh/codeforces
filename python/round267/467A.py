from sys import stdin

n, m, k = list(map(int, stdin.readline().split()))
a = []
for _ in range(m+1):
    a.append(int(stdin.readline()))
res = 0
for i in a[:-1]:
    t = bin(i ^ a[-1])
    count = 0
    for c in t:
        if c == '1':
            count += 1
    if count <= k:
        res += 1
print(res)
