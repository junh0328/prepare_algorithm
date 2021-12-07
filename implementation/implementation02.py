# 시각

N = int(input())

cnt = 0
num = '3'

# range(4) 의 경우 index 3까지 순회하므로 + 1 을 추가하였다
for i in range(N+1):
  for j in range(60):
    for k in range(60):
      # print(i, j, k)
      # 매 시각 안에 '3' 문자열이 포함되어 있다면 카운트 증가
      if num in str(i) + str(j) + str(k):
        cnt += 1

print('cnt:', cnt)