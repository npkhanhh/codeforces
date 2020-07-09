from sys import stdin

n, m = list(map(int, stdin.readline().split()))
a = list(map(int, stdin.readline().split()))
distinct = [0]*n
distinct[-1] = 1
d = {a[-1]: 1}
for i in range(n-2, -1, -1):
    distinct[i] = distinct[i+1]
    if a[i] not in d:
        distinct[i] += 1
        d[a[i]] = 1
for _ in range(m):
    l = int(stdin.readline())
    print(distinct[l-1])
