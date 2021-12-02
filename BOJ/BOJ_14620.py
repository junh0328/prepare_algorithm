# 문제 제목 : 꽃길

# https://www.acmicpc.net/problem/14620

# 전수조사 + 방향벡터에 관한 문제

# N = int(input())

# G = [list(map(int, input().split())) for i in range(N)]

# dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


# def ck(lst):    # a, b, c
#     ret = 0
#     flow = []
#     for flower in lst:
#         x = flower // N
#         y = flower % N
#         if x == 0 or x == N-1 or y == 0 or y == N-1:
#             return 10000

#         for w in range(4):
#             flow.append(x+dx[w], w+dy[w])


# for i in range(N*N):
#     for j in range(N*N):
#         for k in range(N*N):
#             ans = min(ans, ck([i, j, k]))

# print(ans)
