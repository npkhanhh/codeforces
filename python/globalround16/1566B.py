from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    a = s.split('1')
    if len(a) == len(s) + 1:
        print(0)
    elif len(a) == 1 and a[0] == s:
        print(1)
    else:
        a = list(filter(lambda x: len(x) > 0, a))
        if len(a) == 1:
            print(1)
        else:
            print(2)
