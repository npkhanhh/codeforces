from sys import stdin

for _ in range(int(stdin.readline())):
    s = list(input().strip())
    n = len(s)
    res = 'NO'
    for i in range(n):
        if s[n-i-1] != 'a':
            res = 'YES'
            s.insert(i, 'a')
            break
    print(res)
    if res == 'YES':
        print(''.join(s))


