from sys import stdin

n, q = list(map(int, stdin.readline().split()))

a = list(map(int, stdin.readline().split()))
count = [0, 0]
for i in a:
    count[i]+=1
for _ in range(q):
    t, x = list(map(int, stdin.readline().split()))
    if t == 1:
        if a[x-1] == 0:
            count[0] -= 1
            count[1] += 1
        else:
            count[0] += 1
            count[1] -= 1
        a[x-1] = 1 - a[x-1]
    else:
        print(1 if count[1] >= x else 0)
