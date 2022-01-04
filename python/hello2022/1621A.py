from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = n // 2 + n % 2
    if k > a:
        print(-1)
        continue
    for i in range(n):
        s = ['.']*n
        if i % 2 == 0 and k > 0:
            s[i] = 'R'
            k -= 1
        print(''.join(s))


