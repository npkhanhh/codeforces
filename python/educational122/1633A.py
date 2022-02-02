from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n % 7 == 0:
        print(n)
        continue
    for i in range(n-7,n+8):
        if i % 7 == 0 and i // 10 == n //10:
            print(i)
            break
