n = int(input())
for i in range(n):
    word = input()
    len_w = len(word)
    if len_w > 10:
        print(word[0] + str(len_w-2) + word[-1])
    else:
        print(word)