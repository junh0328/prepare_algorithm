# 문제 제목: 수빈이와 수열

# https://www.acmicpc.net/problem/10539

N, B = int(input()), list(map(int, input().split()))

A = [B[0]]

for i in range(1, N):
    # B의 i 번째 자리수 * n으로 나누는 수 - 이전까지의 합계
    A.append(B[i] * (i+1) - sum(A))

for i in A:
    print(i, end=' ')

# 1 2 2 3 4

# A= B[0] 은 고정이다

# B[0] = 1 = 1/1
# B[1] = 2 = (1+x)/2

# >>> 2 * 2 - 1 = x
# >>> 3 = x
