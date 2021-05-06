from sys import stdin

odd = list(range(1, 10001, 2))
even = list(range(2, 10001, 2))
oe = [odd, even]
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        ns = n*n
        switch_point = (ns // 2) - (1 - ns % 2)
        a = [0] * n
        first = 0
        second = 0
        for i in range(n):
            for j in range(n):
                a[j] = oe[first][second]
                second += 1
                if i * n + j == switch_point:
                    first = 1
                    second = 0
            print(*a)
