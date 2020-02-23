def check_distinct(n):
    t = str(n)
    dict = {}
    for c in t:
        if c in dict:
            return False
        else:
            dict[c] = 1
    return True


l, r = list(map(int, input().split()))
res = -1
for i in range(l, r + 1):
    if check_distinct(i):
        res = i
        break
print(res)
