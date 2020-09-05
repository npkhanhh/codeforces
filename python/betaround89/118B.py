n = int(input())
middle = n * 2 + 1
for i in range(n):
    a = ' '.join(list(map(str, range(i))))
    if len(a) > 0:
        a += ' '
    r_a = ' '.join(list(map(str, range(i, -1, -1))))
    spaces = middle - len(r_a)
    print(' ' * spaces + a + r_a)
for i in range(n, -1, -1):
    a = ' '.join(list(map(str, range(i))))
    if len(a) > 0:
        a += ' '
    r_a = ' '.join(list(map(str, range(i, -1, -1))))
    spaces = middle - len(r_a)
    print(' ' * spaces + a + r_a)
