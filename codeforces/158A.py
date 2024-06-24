n, k = [int(i) for i in input().split(' ')]
s = [int(i) for i in input().split(' ')]
k_s = s[-(n-k+1)]

p = [i for i in s if i >= k_s and i > 0]
print(len(p))