n = int(input())
s = input().replace(" ", "")
print(min(s.rfind('0') + 1, s.rfind('1') + 1))