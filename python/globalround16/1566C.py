from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, list(stdin.readline().strip())))
    b = list(map(int, list(stdin.readline().strip())))
    res = 0
    carry = -1
    for i in range(n):
        if a[i] + b[i] == 0:
            res += 1
            if carry == 1:
                res += 1
                carry = -1
            else:
                carry = 0
        elif a[i] + b[i] == 1:
            res += 2
            carry = -1
        else:
            if carry == 0:
                res += 1
                carry = -1
            else:
                carry = 1
    print(res)
