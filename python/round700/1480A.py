from sys import stdin

for _ in range(int(stdin.readline())):
    s = input().strip()
    res = ''
    for idx, val in enumerate(s):
        if idx % 2 == 0:
            if val == 'a':
                res += 'b'
            else:
                res += 'a'
        else:
            if val == 'z':
                res += 'y'
            else:
                res += 'z'
    print(res)
