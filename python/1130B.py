n = int(input())
a = list(map(int, input().split()))
a1 = [False]*n
t1 = n
res = 0
for idx, value in enumerate(a):
    if not a1[value-1]:
        a1[value-1] = True
        t1 -= 1
    if t1 == 0:
        res = idx
        break
print(res+(n*2-1))
