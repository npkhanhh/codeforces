n = int(input())
s = input()
one = s.count('n')
zero = s.count('z')
print(*([1]*one + [0]*zero))
