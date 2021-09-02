input()
a = input().strip()
if len(a) > 26:
    print(-1)
else:
    s = set()

    res = 0
    for i in a:
        if i in s:
            res += 1
        else:
            s.add(i)
    print(res)
