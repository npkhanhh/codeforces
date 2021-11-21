from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    if a[0] == 1:
        print(n+1, *list(range(1, n+1)))
    elif a[-1] == 0:
        print(*list(range(1, n+2)))
    else:
        has_res = False
        for i in range(1, n):
            if a[i] == 1 and a[i-1] == 0:
                print(*list(range(1, i+1)), n+1, *list(range(i+1, n+1)))
                has_res = True
                break
        if not has_res:
            print(-1)
