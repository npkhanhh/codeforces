from sys import stdin

a = [11, 111]
for _ in range(int(stdin.readline())):
    n = int(input())
    res = 'NO'
    while n > 0:
        for i in a:
            if n % i == 0:
                res = 'YES'
        if res == 'YES':
            break
        n -= 11
    print(res)
