# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if '가을' in q1.keys():
    print('q1:', q1['가을'])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if '사과' in q2.values():
    print('q2:', '사과' in q2.values())

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
q3 = 90

if (q3 > 80):
    print('q3:', 'A 학점')
elif (q3 > 60):
    print('q3:', 'B 학점')
elif (q3 > 40):
    print('q3:', 'C 학점')
elif (q3 > 20):
    print('q3:', 'D 학점')
else:
    print('q3:', 'E 학점')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18
max = 0

if (a > b):
    max = a
elif (a < b):
    max = b

if(c > max):
    max = c
    print('q4:', max)

# case 2 다른 풀이

max = a

if b > a:
    max = b
if c > b:
    max = c

print('max:', max)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

q5 = '891022-2473837'


if(q5[7] == '1'):
    print('남자입니다')
elif(q5[7] == '3'):
    print('남자입니다')
elif(q5[7] == '2'):
    print('여자입니다')
elif(q5[7] == '4'):
    print('여자입니다')
else:
    print('잘못된 주민번호입니다')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q6 = ["갑", "을", "병", "정"]
list = []
for v in q6:
    if(v == '정'):
        continue
    list.append(v)

print('q6:', list)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

q7 = []

for v in range(1, 101, 2):
    q7.append(v)

print('q7:', q7)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q8 = ["nice", "study", "python", "anaconda", "!"]
list = []
for v in q8:
    if(len(v) >= 5):
        list.append(v)

print('q8:', list)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q9 = ["A", "b", "c", "D", "e", "F", "G", "h"]
list = []
for v in q9:
    if v.islower():
        list.append(v)

print('q9:', list)


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q10 = ["A", "b", "c", "D", "e", "F", "G", "h"]
list = []

for v in q10:
    if v.isupper():
        list.append(v)
print('q10:', list)
