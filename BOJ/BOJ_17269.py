# 문제 제목: 이름궁합 테스트

# https://www.acmicpc.net/problem/17269

N, M = map(int, input().split())
A, B = input().split()

alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
         3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

AB = ''
min_len = min(N, M)

# 짧은 문자열 길이만큼 더해준다
for i in range(min_len):
    AB += A[i] + B[i]

# AB: LMEIEYSAIWYAUKNI

# 이후 남은 긴 문자열을 뒤에 그대로 더해준다
AB += A[min_len:] + B[min_len:]
# AB: LMEIEYSAIWYAUKNISAKURA
# ord('A') >>> 65

# i 자리에 65를 뺀 값을 넣어준다

lst = [alpha[ord(i)-ord('A')] for i in AB]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1] % 10))


# 8 14
# LEESIYUN MIYAWAKISAKURA
