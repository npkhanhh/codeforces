from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
res = 'NO'
for idx, val in enumerate(a):
    if a[a[val-1]-1] == idx+1:
        res = 'YES'
        break

print(res)
