from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    lock = list(map(int, stdin.readline().split()))
    z = []
    for i in range(n):
        if lock[i] == 0:
            z.append(a[i])
    z.sort(reverse=True)
    j = 0
    for i in range(n):
        if lock[i] == 0:
            a[i] = z[j]
            j += 1
    print(*a)
