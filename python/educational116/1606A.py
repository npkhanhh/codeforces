from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    ab, ba = 0, 0
    for i in range(1, len(s)):
        if s[i-1:i+1] == 'ab':
            ab += 1
        elif s[i-1:i+1] == 'ba':
            ba += 1
    if ab == ba:
        print(s)
    else:
        res = s[:-1]
        res += 'a' if s[-1] == 'b' else 'b'
        print(res)

