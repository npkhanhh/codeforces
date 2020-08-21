from sys import stdin

for _ in range(int(stdin.readline())):
    x, y = list(map(int, stdin.readline().split()))
    print('YES' if x - y > 1 else 'NO')
