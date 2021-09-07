from sys import stdin

xor = [0]*(4*10**5)
cur = 0
for i in range(4*10**5):
    cur ^= i
    xor[i] = cur

for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))
    res = a
    cur = xor[a-1]
    if cur == b:
        print(res)
    else:
        t = b ^ cur
        if t == a:
            res += 2
        else:
            res += 1
        print(res)
