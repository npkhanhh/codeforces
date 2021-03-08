import math


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


n = int(input())
a = set(map(int, input().split()))

gcd = min(a)
for i in a:
    gcd = math.gcd(gcd, i)
    if gcd == 1:
        break

print(len(list(divisorGenerator(gcd))))
