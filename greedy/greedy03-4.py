N, M = map(int, input().split())

result = 0

for _ in range(N):
  lst = list(map(int, input().split()))
  minValue = min(lst)
  result = max(result, minValue)

print(result)