from sys import stdin

d = {'L': 'L', 'R': 'R', 'U': 'D', 'D': 'U'}
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    t = ['a']*n
    for idx, val in enumerate(s):
        t[idx] = d[val]
    print(''.join(t))

