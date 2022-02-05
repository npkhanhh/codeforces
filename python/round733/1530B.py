from sys import stdin


for _ in range(int(stdin.readline())):
    h, w = list(map(int, stdin.readline().split()))
    for i in range(h):
        s = ''
        if i == 0 or i == h-1:
            for j in range(w):
                s += '1' if j % 2 == 0 else '0'
        elif i % 2 == 0 and i != h-2:
            s = '1' + '0'*(w-2) + '1'
        else:
            s = '0'*w
        print(s)
    print()


