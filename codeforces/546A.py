k, n, w = [int(i) for i in input().split(' ')]
print(int(max(0, k * ((w * (w + 1)) / 2) - n)))