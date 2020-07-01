from sys import stdin

for _ in range(int(stdin.readline())):
    v, c, first, second = list(map(int, stdin.readline().split()))
    if v + c >= first + second and min(v, c) >= second:
        print('Yes')
    else:
        print('No')
