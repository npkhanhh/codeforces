from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    v = 200
    i = -1
    for idx, val in enumerate(s):
        if ord(val) < v:
            i = idx
            v = ord(val)
    print(s[i], s[:i]+s[i+1:])

