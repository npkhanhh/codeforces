from sys import stdin

for _ in range(int(stdin.readline())):
    c, d = list(map(int, stdin.readline().split()))
    if abs(c-d) % 2 == 1:
        print(-1)
    elif c == d:
        print([0,1][c>0])
    else:
        print(2)
