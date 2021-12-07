# 1이 될 때까지

N, K = map(int, input().split())

cnt = 0

while True:
  
  target = (N // K) * K
  cnt += (N - target)
  # print('target, cnt', target, cnt)

  N = target
  if N < K:
    break
  cnt += 1
  N //= K

cnt += (N-1)
print(cnt)

# N,K: 17 , 4
# target, cnt: 16 , 1

# N,K: 4 , 4
# target, cnt: 4 , 2

# N,K: 1 , 4
# target, cnt: 0 , 4
# 3
