from sys import stdin

for _ in range(int(stdin.readline())):
    s, a, b, c = list(map(int, stdin.readline().split()))
    res = s // c
    t = res // a
    res += t*b
    print(res)
