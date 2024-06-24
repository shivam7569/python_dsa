m = []
r, c = 0, 0
flag = False
for _ in range(5):
    row = input().split(' ')
    if '1' not in row and not flag: r += 1
    elif '1' in row:
        c = row.index('1')
        flag = True

print(abs(2 - r) + abs(2 - c))