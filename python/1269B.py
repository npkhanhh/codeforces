n, m = list(map(int, input().split()))

s1 = sum(list(map(int, input().split())))
s2 = sum(list(map(int, input().split())))

t = s2 - s1
if t == 0:
    print(0)
elif t > 0:
    res = int((m - t)/(-n))
    print(res)
else:
    res = int((m + t)/n)
    print(res)


