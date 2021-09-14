from sys import stdin

for _ in range(int(stdin.readline())):
    n, s = list(map(int, stdin.readline().split()))
    left = n - n//2 + (1 - n%2)
    print(s//left)


