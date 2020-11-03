s = input()
res = ''
while len(s) > 0:
    t = s[0]
    if t == '.':
        res += '0'
    elif t == '-':
        a = s[1]
        s = s[1:]
        if a == '.':
            res += '1'
        else:
            res += '2'

    s = s[1:]
print(res)
