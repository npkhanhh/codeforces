from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    if a[0] != n and a[-1] != n:
        print(-1)
        continue
    elif a[0] == n:
        print(n, *list(reversed(a[1:])))
    else:
        print(*list(reversed(a[:-1])), n)
