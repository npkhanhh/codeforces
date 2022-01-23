n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
c_a = [0]*2
for i in a:
    c_a[i % 2] += 1
b = list(map(int, input().split()))
c_b = [0]*2
for i in b:
    c_b[i % 2] += 1
print(min(c_a[0], c_b[1]) + min(c_a[1], c_b[0]))


