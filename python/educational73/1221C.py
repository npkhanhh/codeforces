from sys import stdin

for _ in range(int(stdin.readline())):
    c, m, x = list(map(int, stdin.readline().split()))
    print(min(c, m, (c+m+x)//3))
