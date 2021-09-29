from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    c = Counter(stdin.readline().strip())
    print('YES' if c['B'] == c['A'] + c['C'] else 'NO')
