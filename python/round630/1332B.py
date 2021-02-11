from sys import stdin

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    cur_prime = {}
    res = []
    count = 0
    for i in a:
        for j, p in enumerate(primes):
            if i % p == 0:
                if p not in cur_prime:
                    count += 1
                    cur_prime[p] = count
                res.append(cur_prime[p])
                break
    print(count)
    print(*res)

