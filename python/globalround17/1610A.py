from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))
    if a == 1 and b == 1:
        print(0)
    else:
        print(min([a, b, 2]))
