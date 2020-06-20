import math
from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 1:
        print('FastestFinger')
    elif n % 2 == 1 or n == 2:
        print('Ashishgup')
    else:
        n2 = 0
        while n % 2 == 0:
            n //= 2
            n2 += 1
        if n == 1:
            print('FastestFinger')
        else:
            is_prime = True
            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    is_prime = False
            if is_prime and n2 == 1:
                print('FastestFinger')
            else:
                print('Ashishgup')



