from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    t = stdin.readline().strip()
    swapped = False
    res = True
    c1, c2 = '', ''
    for i in range(n):
        if not swapped and s[i] != t[i]:
            if c1 == '':
                c1 = s[i]
                c2 = t[i]
            else:
                if c1 != s[i] or c2 != t[i]:
                    res = False
                    break
                else:
                    c1 = ''
                    c2 = ''
                    swapped = True
        elif swapped and s[i] != t[i]:
            res = False
            break
    if c1 != '':
        res = False
    print('Yes' if res else 'No')


