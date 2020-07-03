for _ in range(int(input())):
    n = int(input())
    print(['NO', 'YES'][360 % (180 - n) == 0])
