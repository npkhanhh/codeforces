from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    c = [0, 0]
    for i in a:
        if 0 <= i <= 1:
            c[i] += 1
    print(c[1]*2**c[0])
