# 숫자 카드 게임

# 2중 반복문 구조를 이용하는 답안 예시

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  # 한 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)