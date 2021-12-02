from sys import stdin

for _ in range(int(stdin.readline())):
    x1, p1 = stdin.readline().split()
    x2, p2 = stdin.readline().split()
    p1 = int(p1)
    p2 = int(p2)
    l1 = len(x1) + p1
    l2 = len(x2) + p2
    if l1 > l2:
        print('>')
    elif l1 < l2:
        print('<')
    else:
        while len(x1) < len(x2):
            x1 += '0'
            p1 -= 1
        while len(x2) < len(x1):
            x2 += '0'
            p2 -= 1
        x1 = int(x1)
        x2 = int(x2)
        if x1 > x2:
            print('>')
        elif x1 < x2:
            print('<')
        else:
            print('=')
