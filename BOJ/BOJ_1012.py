# 문제 제목: 유기농 배추

# https://www.acmicpc.net/problem/1012

# BFS, DFS 둘 다 가능

import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(x, y):
    global B, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)


def process():
    global B, ck
    M, N, K = map(int, input().split())
    B = [[0 for i in range(50+2)] for _ in range(50+2)]
    ck = [[0 for i in range(50+2)] for _ in range(50+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    # DFS 활용
    for i in range(1, M+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1


for _ in range(T):
    process()

# for _ in range() ... 에서 언더바(_)를 쓰는 경우 >>> 안 쓸 변수이기 때문에 굳이 'i'로 나타낼 필요가 없는 경우에 사용
