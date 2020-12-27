from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n > 45:
        print(-1)
    else:
        res = ''
        for i in range(9, 0, -1):
            if n > i:
                res = str(i) + res
                n -= i
            else:
                res = str(n) + res
                break
        print(res)
