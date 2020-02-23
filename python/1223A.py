for _ in range(int(input())):
    n = int(input())
    if n < 4:
        print(4-n)
    elif n % 2 == 1:
        print(1)
    else:
        print(0)