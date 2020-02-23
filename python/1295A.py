for _ in range(int(input())):
    n = int(input())
    res = ''
    if n % 2 == 1:
        res = '7'
        n -= 3
    res += '1'* (n//2)
    print(res)