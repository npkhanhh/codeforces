from sys import stdin

if 0:
    print('hehe')
else:
    print('hoho')

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = []
    for idx, val in enumerate(a[1:], start=1):
        if abs(val - a[idx-1]) > 1:
            res = [idx, idx+1]
            break
    if len(res) == 0:
        print('NO')
    else:
        print('YES')
        print(*res)

