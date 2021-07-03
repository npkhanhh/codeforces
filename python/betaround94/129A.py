n = int(input())
a = list(map(int, input().split()))
t = sum(a) % 2
print(len(list(filter(lambda x: x%2 == t, a))))
