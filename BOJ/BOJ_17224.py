# APC는 왜 서브태스크 대회가 되었을까?

# https://www.acmicpc.net/problem/17224

N, L, K = map(int, input().split())

answer1 = list()
answer2 = list()
cnt = K
sum = 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if cnt >= 0:
        if L >= sub2:
            answer2.append(sub2)
            cnt -= 1
        if L < sub2 and L >= sub1:
            answer1.append(sub1)
            cnt -= 1

sum = len(answer2) * 140 + len(answer1) * 100

print(sum)

# 4 8 4
# 1 8
# 4 5
# 6 20
# 9 12
