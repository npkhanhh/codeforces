from sys import stdin

for _ in range(int(stdin.readline())):
    x, y = list(map(int, stdin.readline().split()))
    s = stdin.readline().strip()
    tx, ty = 0, 0
    for i in s:
        if x < 0 and i == 'L':
            tx -= 1
        if x> 0 and i == 'R':
            tx += 1
        if y < 0 and i == 'D':
            ty -= 1
        if y > 0 and i == 'U':
            ty += 1
    if abs(tx) >= abs(x) and abs(ty) >= abs(y):
        print('YES')
    else:
        print('NO')

