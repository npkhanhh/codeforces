from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(0, 500):
        t = n - 2020*i
        if t < 0:
            print('NO')
            break
        if t % 2021 == 0:
            print('YES')
            break
