from sys import stdin


def factorize(n):
    result = {}
    rest = 1
    for i in [2, 3, 5]:
        while n % i == 0:
            if i not in result:
                result[i] = 1
            else:
                rest *= i
                if rest not in result:
                    result[rest] = 1
                    rest = 1
            n //= i
            if len(result) == 2:
                if n * rest > 1 and n * rest not in result:
                    return list(result.keys()) + [n*rest]
                else:
                    return []
    increments = [4, 2, 4, 2, 4, 6, 2, 6]
    d = 7
    inc = 0
    while d * d <= n:
        while n % d == 0:
            if d not in result:
                result[d] = 1
            else:
                rest *= d
                if rest not in result:
                    result[rest] = 1
                    rest = 1
            n //= d
            if len(result) == 2:
                if n * rest > 1 and n * rest not in result:
                    return list(result.keys()) + [n*rest]
                else:
                    return []
        d += increments[inc]
        inc += 1
        if inc == 8:
            inc = 0
    return []


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = factorize(n)
    if len(res) > 1:
        print("YES")
        print(*res)
    else:
        print("NO")
