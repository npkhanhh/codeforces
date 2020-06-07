from sys import stdin
import queue

n, m = list(map(int, stdin.readline().split()))
a = [0] + list(map(int, stdin.readline().split()))
ma = max(a)
d = {}
visited = [False] * (n + 1)


def min_bfs(node):
    q = queue.Queue()
    q.put(node)
    val = ma
    while not q.empty():
        t = q.get()
        if a[t] < val:
            val = a[t]
        if t in d:
            for z in d[t]:
                if not visited[z]:
                    visited[z] = True
                    q.put(z)
    return val


for _ in range(m):
    t1, t2 = list(map(int, stdin.readline().split()))
    if t1 not in d:
        d[t1] = set()
    d[t1].add(t2)
    if t2 not in d:
        d[t2] = set()
    d[t2].add(t1)

res = 0

for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = True
        res += min_bfs(i)


print(res)

