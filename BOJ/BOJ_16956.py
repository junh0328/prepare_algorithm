# 문제 제목 : 늑대와 양

# https://www.acmicpc.net/problem/16956

R, C = map(int, input().split())
Map = [list(input()) for i in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

check = False

for i in range(R):
    for j in range(C):
        if Map[i][j] == 'W':
            for w in range(4):
                ii, jj = i + dx[w], j + dy[w]
                if ii < 0 or ii == R or jj < 0 or jj == C:
                    continue
                if Map[ii][jj] == 'S':
                    check = True
if check:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if Map[i][j] not in 'SW':
                Map[i][j] = 'D'

for i in Map:
    print(''.join(i))

# 6 6
# ..S...
# ..S.W.
# .S....
# ..W...
# ...W..
# ......
