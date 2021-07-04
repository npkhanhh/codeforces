from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = [0, 0]
    for i in a:
        b[i % 2] += 1
    print('yes' if b[0] == b[1] else 'no')
