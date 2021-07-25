from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a, b = divmod(n, 3)
    if b == 0:
        print(a, a)
    elif b == 1:
        print(a+1, a)
    else:
        print(a, a+1)

