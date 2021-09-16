from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(stdin.readline().strip())
    b = list(stdin.readline().strip())
    res = 0
    for i in range(n):
        if b[i] == '1':
            if i > 0 and a[i-1] == '1':
                res += 1
            elif a[i] == '0':
                res += 1
            elif i < n - 1 and a[i+1] == '1':
                res += 1
                a[i+1] = '2'
    print(res)


