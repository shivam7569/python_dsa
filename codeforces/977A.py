n, k = map(int, input().split())
for _ in range(k):
    n = [n//10, n-1][n%10 > 0]
print(n)