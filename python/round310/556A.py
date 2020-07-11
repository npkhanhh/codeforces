input()
a = [0, 0]
for c in input():
    a[int(c)] += 1
print(abs(a[0]-a[1]))
