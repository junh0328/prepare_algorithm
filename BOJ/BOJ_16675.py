# 문제 제목 : 두 개의 손

# https://www.acmicpc.net/problem/16675

# S : 가위
# R : 바위
# P : 보

# 민성이 또는 태경이가 적절히 왼손 또는 오른손을 선택하여 가위바위보에서 무조건 이기는 방법이 있는지 없는지를 알려고 한다.

lst = list(map(str, input().split()))

MS = lst[:2]
TK = lst[2:]

if len(set(MS)) == 1 and len(set(TK)) == 2:
    # print('M 1 T 2')
    if MS[0] == 'P' and TK[0] or TK[1] == 'S':
        print('TK')
    elif MS[0] == 'R' and TK[0] or TK[1] == 'P':
        print('TK')
    elif MS[0] == 'S' and TK[0] or TK[1] == 'R':
        print('TK')
    else:
        print('?')

elif len(set(TK)) == 1 and len(set(MS)) == 2:
    # print('T 1 M 2')
    if TK[0] == 'P' and MS[0] or MS[1] == 'S':
        print('MS')
    elif TK[0] == 'R' and MS[0] or MS[1] == 'P':
        print('MS')
    elif TK[0] == 'S' and MS[0] or MS[1] == 'R':
        print('MS')
    else:
        print('?')

elif len(set(TK)) == 1 and len(set(MS)) == 1:
    # print('T 1 M 1')
    if TK[0] == 'P' and MS[0] == 'S':
        print('MS')
    elif TK[0] == 'R' and MS[0] == 'P':
        print('MS')
    elif TK[0] == 'S' and MS[0] == 'R':
        print('MS')
    elif MS[0] == 'P' and TK[0] == 'S':
        print('TK')
    elif MS[0] == 'R' and TK[0] == 'P':
        print('TK')
    elif MS[0] == 'S' and TK[0] == 'R':
        print('TK')
    else:
        print('?')

else:
    print('?')


# 무조건 이겨야 하므로 만약 둘 중 한 사람이 가진 경우의 수가 1 일 때 >> 반대 쪽 사람이 이기는 수를 가질 경우 무조건 이긴다
