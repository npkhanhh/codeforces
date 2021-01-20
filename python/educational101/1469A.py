from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().rstrip()
    t = 0
    c = 0
    res = 'YES'
    if len(s) % 2 == 1:
        res = 'NO'
    elif s[0] == ')':
        res = 'NO'
    elif s[-1] == '(':
        res = 'NO'
    print(res)

