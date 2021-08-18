from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = list(stdin.readline().strip())
    if n < 6:
        print(''.join(s))
    else:
        print(''.join(sorted(s)))

