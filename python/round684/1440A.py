from sys import stdin

for _ in range(int(stdin.readline())):
    n, c0, c1, h = list(map(int, stdin.readline().split()))
    count = [0, 0]
    s = stdin.readline().strip()
    for i in s:
        count[int(i)] += 1
    if c0 > h + c1:
        print((h + c1)*count[0] + c1*count[1])
    elif c1 > h + c0:
        print((h + c0)*count[1] + c0*count[0])
    else:
        print(c0*count[0] + c1*count[1])
