# 문제 제목 응계
# 문제 난이도 하
# 문제 유형: 배열, 구현
# 추천 풀이 시간: 15분
# https://www.acmicpc.net/problem/2920


a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

# >>> 1 2 3 4 5 6 7 8 ascending
# >>> 8 7 6 5 4 3 2 1 descending
# >>> 1 3 4 5 6 7 8 2 mixed
