# 1이 될 때까지

N, K = map(int, input().split())

cnt = 0

while True:
  if N == 1 : 
    print(cnt)
    break
  if(N % K == 0):
    N //= K
    cnt +=1
  else:
    N -= 1
    cnt +=1

# 17 4
# 3

# 25 5
# 2