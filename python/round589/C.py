import math

def prime_factors(n):
    res = []
    if n % 2 == 0:
        res.append(2)
    while n % 2 == 0:
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            res.append(i)
        while n % i== 0:
            n = n / i

    if n > 2:
        res.append(n)
    return res

x, n = list(map(int, input().split()))
result = 1
for i in range(1, n+1):
    t = math.gcd(x, i)
    l = prime_factors(t)
    for p in l:
        a = 0
        i1 = i
        while i1 % p == 0:
            a += 1
            i1 /= p
        print(p, i)
        result *= pow(int(p), int(a), 1000000007)
        result %= 1000000007
print(result)


