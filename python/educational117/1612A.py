from sys import stdin

for _ in range(int(stdin.readline())):
    x, y = list(map(int, stdin.readline().split()))
    if (x + y) % 2 == 1:
        print(-1, -1)
    else:
        a, b = divmod(x, 2)
        print(a, y//2 + b)
