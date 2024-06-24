s = input()
l = len(s)

lower = 0
flag = 1
for i in range(l):
    if s[i].islower(): lower += 1
    if lower >= l / 2:
        flag = 0
        break

if flag: s = s.upper()
else: s = s.lower()

print(s)
