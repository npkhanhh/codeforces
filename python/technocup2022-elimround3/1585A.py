from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    cur = 1
    a = list(map(int, stdin.readline().split()))
    cur += a[0]
    for i in range(1, n):
        if a[i] == 1:
            if a[i-1] == 1:
                cur += 5
            else:
                cur += 1
        else:
            if a[i-1] == 0:
                cur = -1
                break
    print(cur)


