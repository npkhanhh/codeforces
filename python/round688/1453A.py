from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    s_a = set()
    for i in a:
        s_a.add(i)

    res = 0
    for i in b:
        if i in s_a:
            res += 1
    print(res)

