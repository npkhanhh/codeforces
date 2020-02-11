n = int(input())
s = input()
if n > 3:
    if n % 2 == 0:
        res = '-'.join(a + b for a, b in zip(s[::2], s[1::2]))
    else:
        res = s[0:3] + '-' + '-'.join(a + b for a, b in zip(s[3::2], s[4::2]))
    print(res)
else:
    print(s)
