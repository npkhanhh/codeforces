from sys import stdin

n = int(stdin.readline())
d = list(map(int, stdin.readline().split()))
a, b = list(map(int, stdin.readline().split()))
print(sum(d[a-1:b-1]))
