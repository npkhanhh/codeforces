from sys import stdin

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    odd = even = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if x == n:
        if odd % 2 == 0:
            print('no')
        else:
            print('yes')
    elif odd > 0 and even > 0:
        print('yes')
    elif even == 0 and x % 2 == 1:
        print('yes')
    else:
        print('no')
