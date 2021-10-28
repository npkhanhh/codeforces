from sys import stdin
from math import gcd, sqrt


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor



for _ in range(int(stdin.readline())):
    count = [0] * 30
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    for i in a:
        b = bin(i)[2:][::-1]
        for j in range(len(b)):
            if b[j] == '1':
                count[29-j] += 1
    res = max(count)
    for i in count:
        if i > 0:
            res = gcd(res, i)
        if res == 1:
            break
    if res == 0:
        print(*list(range(1,n+1)))
    else:
        print(*list(divisorGenerator(res)))
