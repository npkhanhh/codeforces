from sys import stdin

for _ in range(int(input())):
    a, b = sorted(map(int, stdin.readline().split()))
    print(max(2*a, b)**2)
