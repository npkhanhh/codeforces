def solve(n):
    if n % 2 == 1:
        return 0
    res = n//4
    if n % 4 == 0:
        res -= 1
    return res


n = int(input())
print(solve(n))
