from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    print(len(filter(lambda x: x!= 2, map(int, stdin.readline().split()))))
