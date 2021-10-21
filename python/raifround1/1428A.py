from sys import stdin

for _ in range(int(stdin.readline())):
    x1, y1, x2, y2 = list(map(int, stdin.readline().split()))
    offset = 0 if x1 == x2 or y1 == y2 else 2
    print(abs(x2-x1)+abs(y2-y1)+offset)
