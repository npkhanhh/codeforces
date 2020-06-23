from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

t = 0
res = 'YES'
for i in range(1, n):
    if a[i] == a[i-1]:
        if t == 2:
            res = 'NO'
            break
        t = 1
    elif a[i] > a[i-1]:
        if t != 0:
            res = 'NO'
            break
    elif a[i] < a[i-1]:
        t = 2
print(res)
