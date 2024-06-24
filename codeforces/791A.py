from math import log, floor

a, b = [int(i) for i in input().split(' ')]
print(floor(log(b/a)/log(3/2) + 1))