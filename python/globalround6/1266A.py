from sys import stdin

for t in range(int(stdin.readline())):
    z = stdin.readline().rstrip()
    a = list(map(int, list(z)))
    has_0 = False
    even = 0
    for i in a:
        if i == 0:
            has_0 = True
        if i % 2 == 0:
            even += 1
    s = sum(a)
    if s % 3 == 0 and has_0 and even > 1:
        print('red')
    else:
        print('cyan')
