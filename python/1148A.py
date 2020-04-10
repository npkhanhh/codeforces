a, b, c = list(map(int, input().split()))
t = 0 if a == b else 1
print(min(a, b) * 2 + c * 2 + t)
