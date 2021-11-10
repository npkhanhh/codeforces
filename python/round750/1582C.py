from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    t = set(s)
    res = n+1
    while len(t) > 0:
        cur_char = t.pop()
        cur = 0
        l = 0
        r = n-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] == cur_char:
                cur += 1
                l += 1
            elif s[r] == cur_char:
                cur += 1
                r -= 1
            else:
                cur = n+1
                break
        res = min(cur, res)
    if res == n+1:
        print(-1)
    else:
        print(res)

