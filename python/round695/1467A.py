from sys import stdin

s = '989' + '0123456789' * 100000

for _ in range(int(stdin.readline())):
    print(s[:int(stdin.readline())])
