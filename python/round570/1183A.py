def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        s = s % 4
        n //= 10
    return s


n = int(input())

for i in range(10):
    if sum_digits(n + i) % 4 == 0:
        print(n + i)
        break

