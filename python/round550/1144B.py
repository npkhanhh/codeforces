n = int(input())
a = sorted(map(int, input().split()))
b = [[], []]
for i in a:
    b[i % 2].append(i)
if abs(len(b[0]) - len(b[1])) < 2:
    print(0)
else:
    if len(b[1]) < len(b[0]):
        b[0], b[1] = b[1], b[0]
    print(sum(b[1][:(len(b[1]) - len(b[0]) - 1)]))
