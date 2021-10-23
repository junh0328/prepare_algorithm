# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random   # 랜덤으로 불러오기 위함
import time     # 시간 측정을 위함

words = []      # 영어 단어 리스트(1000개 로드)

n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words)    # 단어 리스트 확인

input("Ready? Press Enter Key!")  # Enter Game Start!

start = time.time()  # 시작한 시간 (Start time)

while n <= 5:
    random.shuffle(words)  # words 단어를 섞는다
    q = random.choice(words)  # 뽑아와서 q 에 할당한다

    print()

    print("*Question # {}".format(n))
    print(q)      # 문제 출력

    x = input()   # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():
        print('Pass!')
        cor_cnt += 1
    else:
        print('Wrong!')

    n += 1

end = time.time()       # 끝난 시간 End Time
et = end - start        # 총 게임 시간
et = format(et, ".3f")  # 소숫점 세번째 자리까지 출력

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# 수행 시간 출력
print('게임 시간:', et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass
