for _ in range(int(input())):
    n = int(input())
    sum2 = 3
    i = 2
    while True:
        if n % sum2 == 0:
            print(n//sum2)
            break
        sum2 += 2**i
        i += 1

