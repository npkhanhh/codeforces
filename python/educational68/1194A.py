from sys import stdin

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    print(x*2)
