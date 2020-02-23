for _ in range(int(input())):
    n = int(input())
    s = input()
    x = y = 0
    cm = 1000000
    res = [-1]
    d = {'0_0':1}
    for index, c in enumerate(s):
        if c == 'U':
            y += 1
        elif c == 'R':
            x += 1
        elif c == 'D':
            y -= 1
        elif c == 'L':
            x -= 1
        end = str(x) +'_'+  str(y)
        if end in d:
            if index + 1 - d[end] < cm:
                cm = index + 1 - d[end]
                res = (d[end], index+1)
        d[end] = index+2
    print(*res)
