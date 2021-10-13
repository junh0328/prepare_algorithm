# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print('입력:', sys.stdin.encoding)
print('출력:', sys.stdout.encoding)

# 출력문
print('My name is Junhee Lee')

# 변수 선언
MyName = 'Junhee'

print('Hello', MyName)

# 조건문
if MyName == 'Junhee':
    print('OK,', MyName, 'is right veriable')  # indent, 들여쓰기

# 반복문
"""
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i * j)
"""

# 변수 선언(한글), 가능하지만 쓰지 않는 것을 추천
이름 = '준희'

# 출력
print('Hello', 이름)

# 함수 선언


def 인사(a):
    print('안녕하세요.', a, '님 반갑습니다!')


def greeting():
    print('Hello!')


# 함수 호출
인사('준희')
greeting()

# 클래스


class Cookie:
    pass


# 객체 생성
cookie = Cookie()

# 정보 값 출력
# id, dir은 사용자 정의 함수가 아닌 제공되는 빌트인 메서드이다
print(id(cookie))
print(dir(cookie))
