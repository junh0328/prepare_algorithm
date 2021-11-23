# 제목: 행복
# 문제유형: list, min, max 사용하기
# https://www.acmicpc.net/problem/15969

N, lst = input(), list(map(int, input().split()))

print(max(lst)-min(lst))
