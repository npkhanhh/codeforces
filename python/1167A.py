for _ in range(int(input())):
    n = int(input())
    s = input()
    t = s.find('8')
    if n >= 11 and t > -1 and n - t >= 11:
        print('YES')
    else:
        print('NO')
