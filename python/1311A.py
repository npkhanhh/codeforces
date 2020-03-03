for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a == b:
        print(0)
    elif b > a and (b - a) % 2 == 1:
        print(1)
    elif b < a and (a - b) % 2 == 0:
        print(1)
    else:
        print(2)