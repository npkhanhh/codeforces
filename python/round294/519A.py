
d_b = {
    'q': 9,
    'r': 5,
    'b': 3,
    'n': 3,
    'p': 1
}

d_w = {
    'Q': 9,
    'R': 5,
    'B': 3,
    'N': 3,
    'P': 1
}

b = 0
w = 0
for _ in range(8):
    s = input()
    for c in s:
        if c in d_w:
            w += d_w[c]
        elif c in d_b:
            b += d_b[c]
if b > w:
    print('Black')
elif b < w:
    print('White')
else:
    print('Draw')
