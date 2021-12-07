N, K = map(int, input().split())

cnt = 0

while True:
  print('N,K:', N,',',K)
  target = (N // K) * K
  cnt += (N - target)
  print('target, cnt:', target, ',',cnt)

  N = target
  if N < K:
    break
  cnt += 1
  N //= K
  print()
  
cnt += (N-1)
print(cnt)