n = int(input())
s, r = n // 5, n % 5
s += min(1, r)

print(s)