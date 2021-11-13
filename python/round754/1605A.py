from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = sorted(map(int, stdin.readline().split()))
    if (a + c - 2*b) % 3 == 0:
        print(0)
    else:
        print(1)
