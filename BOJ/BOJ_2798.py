# 문제 제목: 블랙잭
# 문제 난이도: 하
# 문제 유형: 배열, 완전 탐색
# 추천 풀이 시간: 20분

# 첫 번째 인풋 N, M
# 두 번째 인풋 N에 해당하는 카드 배열

n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

answer = 0
length = len(arr)

# print('n=', n, 'max=', m)
# print('arr=', arr)

# 3개를 골라야 함 5C3
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = arr[i] + arr[j] + arr[k]
            if sum <= m:
                answer = max(answer, sum)

print(answer)
