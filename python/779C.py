# n, k = list(map(int, input().split()))
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = sorted(zip(a, b), key=lambda x: x[0] - x[1])
# res = 0
# for idx, value in enumerate(c):
#     if value[0] - value[1] <= 0:
#         res += value[0]
#     elif idx >= k:
#         res += value[1]
#     else:
#         res += value[0]
# print(res)


I = lambda: list(map(int, input().split()))
n, k = I()
a = I()
b = I()
d = sorted([bb-aa for bb, aa in zip(b, a) if bb-aa<0])
f = 0
print(sum(a)+sum(d[:n-k]))