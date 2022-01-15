from sys import stdin

d = {
    'purple': 'Power',
    'green': 'Time',
    'blue': 'Space',
    'orange': 'Soul',
    'red': 'Reality',
    'yellow': 'Mind'
}


n = int(stdin.readline())
for _ in range(n):
    s = stdin.readline().strip()
    if s in d:
        del d[s]
print(len(d))
for v in d.values():
    print(v)
