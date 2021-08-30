a = int(input())
b = int(input())
c = int(input())

t = a
if b < 2*t:
    t = b // 2
if c < 4*t:
    t = c // 4

print(t*7)
