from sys import stdin

for _ in range(int(stdin.readline())):
    l, r = list(map(int, stdin.readline().split()))
    print(l, l*2)
