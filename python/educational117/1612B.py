from sys import stdin

for _ in range(int(stdin.readline())):
    n, a, b = list(map(int, stdin.readline().split()))
    if (a > n // 2) ^ (b <= n // 2):
        print(-1)
        continue
    if a > b + 1:
        print(-1)
        continue
    left = [a] + list(range(max(a + 1, b + 1), n + 1))
    t = n // 2 - len(left)
    for i in range(t):
        left.append(a + i + 1)
    right = [b] + list(range(min(a - 1, b - 1), 0, -1))
    t = n // 2 - len(right)
    for i in range(t):
        right.append(b - i - 1)
    print(*left, *right)
