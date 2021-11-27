# APC는 왜 서브태스크 대회가 되었을까?

# https://www.acmicpc.net/problem/17224

N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if L >= sub2:
        hard += 1
    if L < sub2 and L >= sub1:
        easy += 1

# hard 문제
answer = min(hard, K) * 140

# easy 문제

if hard < K:
    answer += min(K-hard, easy) * 100

print(answer)

# 4 8 4
# 1 8
# 4 5
# 6 20
# 9 12
