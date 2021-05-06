from sys import stdin
from collections import defaultdict

d = defaultdict(list)
n, m = list(map(int, stdin.readline().split()))
a = [0] + list(map(int, stdin.readline().split()))
for _ in range(n - 1):
    x, y = list(map(int, stdin.readline().split()))
    d[x].append(y)
    d[y].append(x)
s = []
dp = [0] * (n + 1)
dp[1] = a[1]
s.append(1)
res = 0
visited = [False] * (n + 1)
visited[1] = True
while len(s) > 0:
    cur = s.pop()
    temp = d[cur]
    is_leaf = True
    for node in temp:
        if visited[node]:
            continue
        visited[node] = True
        is_leaf = False
        if a[node] == 1:
            dp[node] = dp[cur] + a[node]
        if dp[node] > m:
            continue
        s.append(node)
    if is_leaf:
        res += 1

print(res)

