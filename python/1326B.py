n = int(input())
b = list(map(int, input().split()))
a = [b[0]]
max_a = b[0]
for i in range(1, n):
    a.append(max_a+b[i])
    max_a = max(max_a, a[-1])
print(*a)