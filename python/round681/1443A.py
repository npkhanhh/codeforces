from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = []
    for i in range(n):
        a.append(n*4 - 2*i)
    print(*a)
