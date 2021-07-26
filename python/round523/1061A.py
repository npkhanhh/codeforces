n, s = list(map(int, input().split()))
res = s // n
if s % n != 0:
    res += 1
print(res)
