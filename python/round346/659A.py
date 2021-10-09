

n, a, b = list(map(int, input().split()))

a -= 1
a += b
a %= n
a+=1


print(a)
