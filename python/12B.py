n = input()
m = input()
if len(n) > 1:
    others = []
    z = []
    for i in n:
        if i == '0':
            z.append(i)
        else:
            others.append(i)
    others = sorted(others)

    n = others[0] + ''.join(z) + ''.join(others[1:])

print('OK' if n == m else 'WRONG_ANSWER')