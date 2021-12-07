# 상하좌우

N = int(input())
lst = list(map(str, input().split()))

start = [1,1]

for i in range(len(lst)):
    if lst[i] == 'L' :
      if start[1] -1 == 0:
        continue
      start[1] -= 1
    elif lst[i] == 'R' :
      if start[1] +1 == N:
        continue
      start[1] += 1
    elif lst[i] == 'U' :
      if start[0] -1 == 0:
        continue
      start[0] -= 1
    elif lst[i] == 'D' :
      if start[0] + 1 == N:
        continue
      start[0] += 1
    else:
      continue

print(start)