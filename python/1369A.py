from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n % 4 == 0:
        print('YES')
    else:
        print('NO')
