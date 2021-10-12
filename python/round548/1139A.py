from sys import stdin


stdin.readline()
res = 0
a = list(map(int, list(stdin.readline().strip())))

for idx, val in enumerate(a):
    if val % 2 == 0:
        res += idx+1
print(res)
