for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()), reverse=True)
    res = 0
    if a > 0:
        res += 1
        a -= 1
    if b > 0:
        res += 1
        b -= 1
    if c > 0:
        res += 1
        c -= 1
    if a > 0 and b > 0:
        res += 1
        a -= 1
        b -= 1
    if a > 0 and c > 0:
        res += 1
        a -= 1
        c -= 1
    if b > 0 and c > 0:
        res += 1
        b -= 1
        c -= 1
    if a > 0 and b > 0 and c > 0:
        res += 1
    print(res)

# from bisect import bisect
# l = '001 011 022 122 223 333 444'.split()
# for _ in range(int(input())): print(bisect(l, '{}{}{}'.format(*sorted(min(int(s), 4) for s in input().split()))))