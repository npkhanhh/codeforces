from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = list(map(int, stdin.readline().split()))
    total = a + 2*b + 3*c
    print(total % 2)
