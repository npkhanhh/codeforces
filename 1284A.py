n, m = list(map(int, input().split()))

s = input().split()
t = input().split()
q = int(input())
for _ in range(q):
    y = int(input())
    print(s[y%n-1]+t[y%m-1])