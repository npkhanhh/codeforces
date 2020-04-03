n = int(input())
a = []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append((x, y))
k = int(input())
for idx, val in enumerate(a):
    if val[0] <= k <= val[1]:
        print(n - idx)
        break
