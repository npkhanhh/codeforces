from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))
    print(a ^ b)
