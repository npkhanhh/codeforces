from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = stdin.readline().strip()
    b = stdin.readline().strip()
    res = 'YES'
    for i in range(n):
        if a[i] == b[i] == '1':
            res = 'NO'
            break
    print(res)
