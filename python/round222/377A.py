from sys import stdin
import queue

n, m, k = list(map(int, stdin.readline().split()))
a = [['a'] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
s = 0
start = (-1, -1)
for i in range(n):
    a[i] = list(stdin.readline().rstrip())
    if k > 0:
        for j in range(m):
            if a[i][j] == '.':
                s += 1
                start = (i, j)

d = s - k
if k > 0 and d > 0:
    q = queue.Queue()
    q.put(start)
    visited[start[0]][start[1]] = True
    d -= 1
    while d > 0:
        cur = q.get()
        i, j = cur
        if i > 0 and a[i - 1][j] == '.' and not visited[i - 1][j]:
            q.put((i - 1, j))
            visited[i - 1][j] = True
            d -= 1
            if d == 0:
                break
        if j > 0 and a[i][j - 1] == '.' and not visited[i][j - 1]:
            q.put((i, j - 1))
            visited[i][j - 1] = True
            d -= 1
            if d == 0:
                break
        if i < n - 1 and a[i + 1][j] == '.' and not visited[i + 1][j]:
            q.put((i + 1, j))
            visited[i + 1][j] = True
            d -= 1
            if d == 0:
                break
        if j < m - 1 and a[i][j + 1] == '.' and not visited[i][j + 1]:
            q.put((i, j + 1))
            visited[i][j + 1] = True
            d -= 1
            if d == 0:
                break

    for i in range(n):
        for j in range(m):
            if a[i][j] == '.' and not visited[i][j]:
                a[i][j] = 'X'
for row in a:
    print(''.join(row))
