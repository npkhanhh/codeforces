from sys import stdin

sieve = [False] * (10 ** 7)
primes = [0] * (10 ** 5 + 1)
idx_prime = 0
for i in range(2, 1299722):
    if not sieve[i]:
        sieve[i] = True
        primes[idx_prime] = i
        idx_prime += 1
        if idx_prime >= 10 ** 5 + 1:
            break
        cur = i + i
        while cur < 1299722:
            sieve[cur] = True
            cur += i
n = int(stdin.readline())
print(*primes[:n])
