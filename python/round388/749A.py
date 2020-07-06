n = int(input())
if n % 2 == 0:
    res = n // 2
    print(res)
    print(*([2]*res))
else:
    n -= 3
    res = n // 2
    print(res + 1)
    t = [2]*res
    t.append(3)
    print(*t)
