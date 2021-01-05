from sys import stdin

for _ in range(int(stdin.readline())):
    x, y = list(map(int, input().split()))
    print(x - 1, y)
