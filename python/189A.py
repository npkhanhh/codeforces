n, a, b, c = list(map(int, input().split()))
table = [0] + [float('-inf')]*5000
for i in range(1, n+1):
    table[i] = max(table[i-a], table[i-b], table[i-c])+1
print(table[n])
