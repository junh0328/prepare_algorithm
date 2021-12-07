# 숫자 카드 게임

N, M = map(int, input().split())
lst = []
min = 0

for _ in range(N) :
  immsi = (list(map(int, input().split())))
  lst.append(sorted(immsi))

for i in range(len(lst)):
    if i + 1 >= len(lst):
        break
    else:
        if (lst[i][0]) < (lst[i+1][0]):
            min = lst[i+1]

print(min[0])

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4

# 3