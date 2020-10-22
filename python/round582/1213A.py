input()
a = list(map(int, input().split()))

odd_even = [0, 0]
for i in a:
    odd_even[i % 2] += 1
print(min(odd_even))
