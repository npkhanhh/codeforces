from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    n = len(s)
    if n % 2 == 1:
        print('NO')
        continue
    print('YES' if s[:n//2] == s[n//2:] else 'NO')
