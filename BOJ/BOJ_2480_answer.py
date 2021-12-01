# 문제 제목: 주사위 세개

# https://www.acmicpc.net/problem/2480

lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:
    print(10000 + lst[0] * 1000)
elif len(set(lst)) == 2:
    print(1000 + lst[1]*100)
else:
    print(lst[2] * 100)
