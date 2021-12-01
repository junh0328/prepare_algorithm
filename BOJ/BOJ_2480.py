# 문제 제목: 주사위 세개

# https://www.acmicpc.net/problem/2480

a, b, c = map(int, input().split())

cnt = 0
lst = list()

lst.append(a)
lst.append(b)
lst.append(c)

for i in range(len(lst)):
    if i+1 >= len(lst):
        break
    if lst[i] == lst[i+1]:
        cnt += 1


if cnt == 1:
    print(min(lst)*100 + 1000)
elif cnt == 2:
    print(max(lst)*1000 + 10000)
else:
    print(max(lst)*100)

# 시간 초과로 틀림

# 1. 중복 된 값을 확인하기 위해서는 set을 통해 받는 방법을 사용해 볼 필요가 있다
# 2. a, b, c를 각각 받아서 lst 배열에 넣는 것 보다, 처음부터 배열로 받는 방법을 사용할 것
# 3. 입력받은 배열을 sorted 메서드를 통해 정렬하면, 중복된 lst 배열에 대해서 리스트 슬라이싱하기가 편하다
