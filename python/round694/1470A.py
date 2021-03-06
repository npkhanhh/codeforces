from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    k = sorted(list(map(int, stdin.readline().split())), reverse=True)
    c = list(map(int, stdin.readline().split()))
    res = 0
    j = 0
    for i in k:
        if c[i-1] > c[j]:
            res += c[j]
            j += 1
        else:
            res += c[i-1]
    print(res)
