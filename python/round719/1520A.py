from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    d = {s[0]: 1}
    res = 'YES'
    for idx, val in enumerate(s[1:], start=1):
        if val != s[idx - 1]:
            c = s[idx - 1]
            if val in d:
                res = 'NO'
                break
            else:
                d[c] = 1

    print(res)
