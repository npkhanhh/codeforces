from sys import stdin


for _ in range(int(stdin.readline())):
    x1, y1, x2, y2 = list(map(int, stdin.readline().split()))
    print((x2-x1)*(y2-y1)+1)
