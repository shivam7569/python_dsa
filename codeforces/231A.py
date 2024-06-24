n = int(input())
k = 0
for i in range(n):
    s = sum([int(i) for i in input().split(' ')])
    if s > 1: k += 1

print(k)