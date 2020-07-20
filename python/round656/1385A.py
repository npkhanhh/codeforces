from sys import stdin

for _ in range(int(stdin.readline())):
    x, y, z = sorted(map(int, stdin.readline().split()))
    if y == z:
        print('YES')
        print(z, x, x)
    else:
        print('NO')
