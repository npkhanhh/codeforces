from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c, d = list(map(int, stdin.readline().split()))
    print(max(a + b, c + d))
