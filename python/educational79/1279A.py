from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = sorted(list(map(int, stdin.readline().split())))
    if a + b >= c-1:
        print('Yes')
    else:
        print('No')

