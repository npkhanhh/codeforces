from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    curchar = 0
    s = chr(curchar+97) * 200
    print(s)
    for i in a:
        curchar = (curchar + 1) % 26
        if s[i] == chr(curchar + 97):
            curchar = (curchar + 1) % 26
        t = s[:i] + chr(curchar + 97) * (200 - i)
        print(t)
        s = t
