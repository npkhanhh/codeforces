from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    a = 0
    b = 0
    res = 0
    for i in s:
        if i == '(':
            a+= 1
        elif i == '[':
            b += 1
        elif i == ')' and a > 0:
            a -= 1
            res += 1
        elif i == ']' and b > 0:
            b -= 1
            res += 1
    print(res)
