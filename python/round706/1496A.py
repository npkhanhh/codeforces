from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    s = stdin.readline().strip()
    if k == 0:
        print('YES')
        continue
    if k * 2 == n:
        print('NO')
        continue
    print('YES' if s[:k] == s[:-k-1:-1] else 'NO')
