from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 0
    temp = 0
    for i in a:
        if i + temp >= 0:
            temp += i
        else:
            res += abs(i) - temp
            temp = 0
    print(res)
