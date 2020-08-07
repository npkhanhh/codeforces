from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    m_a = min(a)
    m_b = min(b)
    res = 0
    for i in range(n):
        res += max(a[i] - m_a, b[i] - m_b)
    print(res)
