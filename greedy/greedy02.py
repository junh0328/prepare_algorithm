N, M, K = map(int, input().split())

immsi = K

lst = list(map(int, input().split()))
sum = 0

lst = sorted(lst, reverse=True)
# print('lst:', lst)

for _ in range(M):
    if K != 0 :
        K -= 1
        sum += lst[0]
    else:
        K = immsi
        sum += lst[1]
    # print('sum:', sum)

print(sum)

# 5 8 3
# 2 4 5 4 6

# 46

# 5 7 2
# 3 4 3 4 3

# 28