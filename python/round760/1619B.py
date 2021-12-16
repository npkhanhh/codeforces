from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = stdin.readline().split()
    res = a[0]

    for i in range(1, len(a)):
        if a[i][0] != a[i-1][1]:
            res += a[i][0]
        res += a[i][1]
    if len(res) != n:
        res += 'a'
    print(res)

