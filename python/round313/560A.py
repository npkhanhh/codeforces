n = int(input())
a = list(map(int, input().split()))

has_1 = False

for i in a:
     if i == 1:
         has_1 = True
         break
print(-1 if has_1 else 1)
