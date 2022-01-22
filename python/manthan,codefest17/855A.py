from sys import stdin

se = set()
for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    if s in se:
        print('YES')
    else:
        print('NO')
        se.add(s)


