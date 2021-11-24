# 문제 제목: 보너스 점수

# https://www.acmicpc.net/problem/17389

N, S = input(), input()

score, bonus = 0, 0

for idx, OX in enumerate(S):
    if OX == 'O':
        score += idx + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(score)

# input

# 8
# XOOOXOOX


# enumerate

# idx: 0 OX: X
# idx: 1 OX: O
# idx: 2 OX: O
# idx: 3 OX: O
# idx: 4 OX: X
# idx: 5 OX: O
# idx: 6 OX: O
# idx: 7 OX: X
