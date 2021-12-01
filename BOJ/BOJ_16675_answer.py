# 문제 제목 : 두 개의 손

# https://www.acmicpc.net/problem/16675

# S : 가위
# R : 바위
# P : 보

# 민성이 또는 태경이가 적절히 왼손 또는 오른손을 선택하여 가위바위보에서 무조건 이기는 방법이 있는지 없는지를 알려고 한다.

# 무조건 이겨야 하므로 만약 둘 중 한 사람이 가진 경우의 수가 1 일 때 >> 반대 쪽 사람이 이기는 수를 가질 경우 무조건 이긴다

# 반복문을 돌면서 튜플을 만든다

ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())
# ML, MR, TL, TR = ('SPR'.find(i) for i in input().split())

print(ML, MR, TL, TR)

if ML == MR and (ML+2) % 3 in [TL, TR]:
    print('TK')
elif TL == TR and (TL+2) % 3 in [ML, MR]:
    print('MS')

else:
    print('?')
