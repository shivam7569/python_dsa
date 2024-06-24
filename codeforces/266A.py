n = int(input())
s = input()
k = 0

for i in range(1, n):
    if s[i] == s[i-1]: k += 1

print(k)