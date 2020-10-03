a = list(map(int, list(input().rstrip())))
res = ''
t = 0
if a[0] == 9:
    res += '9'
    t = 1
for i in a[t:]:
    if i >= 5:
        res += str(9-i)
    else:
        res += str(i)
print(res)



