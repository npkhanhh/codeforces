from sys import stdin

for _ in range(int(stdin.readline())):
    s = list(stdin.readline().strip())
    has_res = True
    for idx, val in enumerate(s):
        t = {'a', 'b', 'c'}
        if val == '?':
            if idx > 0 and s[idx-1] in t:
                t.remove(s[idx-1])
            if idx < len(s) - 1 and s[idx+1] in t:
                t.remove(s[idx+1])
            s[idx] = t.pop()
        if idx > 0 and val != '?' and val == s[idx-1]:
            has_res = False
            break
    if has_res:
        print(''.join(s))
    else:
        print(-1)



