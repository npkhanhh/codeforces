from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline().split()
    a = list(map(int, stdin.readline().split()))
    res = []
    reversed_res = []
    for i in a:
        if len(reversed_res) == 0:
            reversed_res.append(i)
        elif i < reversed_res[-1]:
            reversed_res.append(i)
        else:
            res.append(i)
    res = reversed_res[::-1]+res
    print(*res)
