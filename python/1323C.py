n = int(input())
s = input()
res = 0
cur = 0
l = 0
need_reorder = False
for i in s:
    if i == ')':
        cur-=1
        if cur < 0:
            need_reorder = True
    if need_reorder:
        l += 1
    if i == '(':
        cur += 1
        if cur == 0 and need_reorder:
            res += l
            l = 0
            need_reorder = False
if cur != 0:
    print(-1)
else:
    print(res)


