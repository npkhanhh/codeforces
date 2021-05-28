from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    t = 100
    for i in range(100, 1, -1):
        if n % i == 0 and 100 % i == 0:
            t //= i
            break
    print(t)
