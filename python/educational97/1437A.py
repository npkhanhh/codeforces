from sys import stdin

for _ in range(int(stdin.readline())):
    l, r = list(map(int, stdin.readline().split()))
    if r / 2 >= l:
        print('NO')
    else:
        print('YES')
