from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, n = list(map(int, stdin.readline().split()))
    n = n % 3
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a^b)
