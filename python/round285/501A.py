from sys import stdin

a, b, c, d = list(map(int, stdin.readline().split()))

m = max((3*a)//10, a - (a*c) // 250)
v = max((3*b)//10, b - (b*d) // 250)
if m > v:
    print('Misha')
elif v > m:
    print('Vasya')
else:
    print('Tie')
