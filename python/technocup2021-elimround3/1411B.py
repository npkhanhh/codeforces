from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    while True:
        t = n
        is_res = True

        while t > 0:
            a = t % 10
            if a != 0 and n % a != 0:
                is_res = False
                break
            t //= 10
        if is_res:
            break
        n += 1
    print(n)
