from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = list(map(int, stdin.readline().split()))
    t1 = 1 if a < c else -1
    t2 = b if c < a*b else -1
    print(t1, t2)
