from sys import stdin

from queue import Queue

n = int(stdin.readline())
a = [[] for _ in range(n + 1)]
e = [-1] * (n + 1)

for _ in range(n - 1):
    u, v = list(map(int, stdin.readline().split()))
    a[u].append(v)
    a[v].append(u)
q = Queue()
visited = [False] * (n + 1)

for i, v in enumerate(a):
    if len(v) == 1 and i != 1:
        e[i] = 0
        visited[i] = True
        if v[0] != 1:
            q.put(v[0])
            visited[v[0]] = True
while not q.empty():
    v = q.get()
    s = 0
    count = 0
    un_cal = 0
    parent = -1
    for i in a[v]:
        if e[i] > -1:
            s += e[i] + 1
            count += 1
        else:
            un_cal += 1
            parent = i
    if un_cal > 1:
        print(v)
        q.put(v)
        continue
    if parent > 1 and not visited[parent]:
        visited[parent] = True
        q.put(parent)
    e[v] = (s / count)
s = 0
count = 0
for i in a[1]:
    s += e[i] + 1
    count += 1
print(s / count)
