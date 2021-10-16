# Section05-1
# 파이썬 흐름제어(제어문)

# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
    print('참 입니다!')

# 예2
if False:
    print('거짓 입니다')
else:
    print('참 입니다!')

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

print()

# 참 거짓 종류 (True, False)

# 참 : '내용', [내용], (내용), {내용}, 1 >>> 내용이 있는 자료형
# 거짓 : '', [], (), {}, 0 >>> 내용이 없는 자료형

city = ''

if(city):
    print(city)
else:
    print('city가 빈 문자열입니다')

print()

# 논리 연산자
# and, or, not 문자 그대로 사용

a = 100
b = 60
c = 15

print('and: ', a > b and b > c)
print('or: ', a > b or c > b)  # 둘 중 하나만 만족하더라도 true
print('not:', not a > b)
print('"not False:" ', not False)
print('"Ænot True:" ', not True)

print()

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용 (우선순위)

print('ex1 :', 5+10 > 0 and 7 + 3 == 10)

score1 = 90
score2 = 'A'

print()

if score1 >= 90 and score2 == 'A':
    print('합격')
else:
    print('불합격입니다')

# 다중 조건문

num = 2

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print('num 등급 D, 탈락', num)

print()

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print('A지망 지원 가능')
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")
