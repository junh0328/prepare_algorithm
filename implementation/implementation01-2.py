# 상하좌우

# x,y 좌표를 리스트로 만들지 않았음
# plans 라는 'L' 'R' 'U' 'D' 또한 리스트로 만들지 않음

n = int(input())
x, y = 1, 1
plans = input().split()


# L, R, U, D에 따른 이동 방향

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하니씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = x + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

print(x,y)

# 5
# R R U D D

# >>> plans = R R U D D