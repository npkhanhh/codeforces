from sys import stdin

for _ in range(int(stdin.readline())):
    x, n = list(map(int, stdin.readline().split()))
    t = n % 4
    for i in range(n-t+1, n+1):
        if x % 2 == 0:
            x -= i
        else:
            x += i
    print(x)
