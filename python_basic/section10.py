# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요하다
# linter : 코드 스타일, 문법 체크

# ① SyntaxError (문법 에러) : 잘못된 문법

# print('Test)
# SyntaxError: unterminated string literal (detected at line 10)

# if True >>> SyntaxError: expected ':'
#  pass
# x => y

# ② NameError : 참조 변수가 없을 때 생기는 에러

import time

a = 10
b = 15

# print(c)
# NameError: name 'c' is not defined

# ③ ZeroDivisionError : 0 나누기 에러

# print(10 / 0)
# ZeroDivisionError: division by zero

# ④ IndexError : 인덱스 범위가 오버(넘쳤을)됐을 때

x = [10, 20, 30]
print(x[0])
# print(x[3]) >>> IndexError: list index out of range

# ⑤ KeyError (Dictionaries에 Key가 없을 때)

dic = {'name': 'Kim', 'Age': 33, 'city': 'Seoul'}
# print(dic['hobby']) >>> KeyError: 'hobby'

print(dic.get('hobby'))  # >>> None

# ⑥ AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

# import time

print(time.time())
# print(time.month()) >>> AttributeError: module 'time' has no attribute 'month'

# ⑦ valueError : 참조 값이 없을 때 발생

x = [1, 5, 9]

# x.remove(10)  >>> ValueError: list.remove(x): x not in list
# x.index(10)

# ⓼ FileNotFoundError 경로를 찾을 수 없을 때

# f = open('test.txt', 'r') >>> FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# ⑨ TypeError

x = [1, 2]
y = (3, 4, 5)
z = 'test'

# print(x + y) >>> TypeError: can only concatenate list (not "tuple") to list
# print(x + z)

# 따라서 형 변환이 필요하다
print(x + list(y))

# 항상 예외가 발새앟지 않을 것으로 가정하고 먼저 코딩을 해야 한다!
# 그 후 런타임 예외 발생시 예외 처리 코딩하는 단계를 권장한다(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1

# name = ['kim', 'lee', 'park']

# try:
#     z = 'kim'
#     # z = 'shin'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except ValueError:
#     print('Not Found it! - Occured valueError! ')
# else:
#     print('Ok! else!')

print()

# 예제 2

name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    # z = 'shin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:  # Error 의 종류를 적지 않으면 모든 Error가 해당 except로 들어온다
    print('Not Found it! - Occured valueError! ')
else:
    print('Ok! else!')
