import re
from sys import stdin

for _ in range(int(stdin.readline())):
    a = sorted(re.split('0+', stdin.readline().rstrip()), reverse=True)
    print(sum([len(x) for x in a[::2]]))
