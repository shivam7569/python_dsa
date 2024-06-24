n = int(input())
k = 0
for i in range(n):
    o = input()
    if '+' in o: k += 1
    else: k -= 1

print(k)