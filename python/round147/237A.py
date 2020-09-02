from sys import stdin

n = int(stdin.readline())
t = 1
res = 1
h_prev, m_prev = list(map(int, stdin.readline().split()))
for _ in range(n - 1):
    h, m = list(map(int, stdin.readline().split()))
    if h == h_prev and m == m_prev:
        t += 1
        if t > res:
            res = t
    else:
        t = 1
    h_prev, m_prev = h, m
print(res)
