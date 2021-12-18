from sys import stdin

for _ in range(int(stdin.readline())):
    s = sorted(list(stdin.readline().strip()))
    t = stdin.readline().strip()
    has = [False]*3
    count = [0]*3
    for i in s:
        if i == 'a':
            count[0] += 1
            has[0] = True
        elif i == 'b':
            count[1] += 1
            has[1] = True
        elif i == 'c':
            count[2] += 1
            has[2] = True
    has_three = all(has)
    if t != 'abc' or not has_three:
        print(''.join(s))
        continue
    res = ''.join(s[:count[0]]) + 'c'*count[2] + 'b'*count[1] + ''.join(s[sum(count):])
    print(res)
