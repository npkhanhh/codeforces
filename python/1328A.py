import math

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    print(int(math.ceil(a/b)*b-a))