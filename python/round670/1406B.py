from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    res = a[-1]
    i = 0
    j = -2
    for _ in range(2):
        if res * a[i] * a[i+1] > res * a[j] * a[j-1]:
            res *= a[i] * a[i+1]
            i += 2
        else:
            res *= a[j] * a[j-1]
            j -= 2
    print(res)

