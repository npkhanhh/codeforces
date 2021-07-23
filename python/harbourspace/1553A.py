from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    print(n//10 + (1 if (n % 10 == 9) else 0))
