# 왕실의 나이트

# row 행
# column 열

input = input()
x = int(ord(input[0])) - int(ord('a')) + 1
y = int(input[1])

# print(x,y)
# a1
# 1 1

# 완전 탐색을 위해 방향을 잡는 것이 가장 중요
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2,1), (1,2), (-1,2), (-2,1)]

cnt = 0
for step in steps:
  # 다음에 갈 x 좌표 방향
  next_x = x + step[0]
  # 다음에 갈 y 좌표 방향
  next_y = y + step[1]

  # 다음에 갈 방향이 체스판의 범위를 넘지 않을 경우에만 증감시키기
  if next_x >= 1 and next_x <= 9 and next_y >= 1 and next_x <= 8:
    cnt += 1
  
print('cnt:', cnt)

# a1
# 2

# c2
# 6