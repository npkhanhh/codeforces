n = int(input())
a = sorted(map(int, input().split()))
total = sum(a)
res = total
if n > 1:
    for idx, val in enumerate(a):
        if n - idx < 3:
            res += total
            break
        res += val
        total -= val
        res += total
print(res)
