from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    c = list(sorted(zip(a, b)))
    for ai, bi in c:
        if ai <= k:
            k += bi
        else:
            break
    print(k)
