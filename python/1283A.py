n = int(input())

for i in range(n):
    h, m = list(map(int, input().split()))
    res = 0
    if m == 0:
        res = (24 - h) * 60
    else:
        res = (23 - h) * 60 + (60 - m)
    print(res)

