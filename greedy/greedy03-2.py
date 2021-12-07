# 숫자 카드 게임

# min() 함수를 이용하는 답안 예시

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  # 한 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)