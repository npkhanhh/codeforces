from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(n):
        left = n - i
        print('('*i + '()'*(n-i) + ')'*i)
