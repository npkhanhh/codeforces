I = lambda: int(input())
a = I()
b = I()
c = I()
d = I()
e = I()
f = I()

if e >= f:
    suit1 = min(a, d)
    suit2 = min(b, c, d - suit1)
    print(suit1 * e + suit2 * f)
else:
    suit2 = min(b, c, d)
    suit1 = min(a, d - suit2)
    print(suit1 * e + suit2 * f)

