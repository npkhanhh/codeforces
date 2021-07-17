from sys import stdin
import math

for _ in range(int(input())):
    n = int(input())
    print(int(math.ceil(sum(map(int, stdin.readline().split()))/n)))
