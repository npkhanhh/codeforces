from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    if k > n:
        print(k-n)
    elif n % 2 != k % 2:
        print(1)
    else:
        print(0)
