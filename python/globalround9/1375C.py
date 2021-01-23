from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    a = list(map(int, stdin.readline().split()))
    if a[0] < a[-1]:
        print("YES")
    else:
        print("NO")



