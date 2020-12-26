from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = sorted(map(int, stdin.readline().split()))
    print(max(c - b - a + 1, 1))
