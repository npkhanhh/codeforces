for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print('2' + '9' * (n - 1))
