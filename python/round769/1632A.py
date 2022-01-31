from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    if n == 1:
        print('YES')
        continue
    if n == 2 and s[0] != s[1]:
        print('YES')
        continue
    print('NO')
