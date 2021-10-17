
# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출

# 함수명()
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제 1

# hello('에러') >>> NameError: name 'hello' is not defined.

def hello(world):
    print('Hello', world)


hello('준희!')
hello('Python!')
hello(7777)

print()

# 예제 2 (리턴 사용)


def hello_return(world):
    val = 'Hello' + str(world)
    return val


str = hello_return('Junhee')

print(str)

print()

# 예제 3 (다중 리턴)


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제 4 (데이터 타입 반환)
# 리스트 타입


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul2(100)
print(lt)

# 튜플 타입


def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)


tp = func_mul3(100)
print(tp)

print()

# 예제 5
# *args (arguments), *kwargs (keyword arguments)

# *args >> 가변 (JS의 REST Parameter와 동일)
# 튜플의 형태로 넘어온다


def args_func(*args):
    # print(type(args))
    print(args)

# 따라서 반복문을 사용할 수도 있다


def args_func2(*args):
    for t in args:
        print(t)

# enumerable >>> 인덱스를 통해 인덱스와 요소를 열거


def args_func3(*args):
    # for i, v in enumerate(range(10)) 범위 설정도 가능
    for i, v in enumerate(args):
        print(i, v)


args_func('kim')
args_func('kim', 'lee')
args_func('kim', 'lee', 'park')

args_func2('kim', 'lee', 'park')

args_func3('kim', 'lee', 'park')

print()

# kwargs


def kwargs_func(**kwargs):
    print(kwargs)


def kwargs_func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1='Kim', name2='Park', name3='Lee')
kwargs_func2(name1='Kim', name2='Park', name3='Lee')

print()

# 전체 혼합


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(1, 2)  # 1 2 () {}
example_mul(1, 2, 3)  # 1 2 (3) {}
example_mul(1, 2, 3, 4, name1='kim', name2='lee')  # 1 2 (3, 4) {'name': 'kim'}

print()

# 중첩함수(클로저)


def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print('in func')
    func_in_func(num + 1000)


nested_func(1000)

# 예제 6 힌트 (타입 설정 but, 타입이 다르더라도 에러를 발생시키지는 않는다)


def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(5))
print(func_mul3(6.0))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적인 함수 -> 변수 할당


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)  # <function mul_10 at 0x10abb6830> 함수 선언시에 메모리에 이미 할당되어 있다
print(type(var_func))  # <class 'function'>

print(var_func(10))

# 람다식
# 불필요한 리턴문을 다 없앰, 메모리에 할당되지 않음

# lambda_mul_10= lambda num: num * 10


def lambda_mul_10(num): return num * 10


print('>>>', lambda_mul_10(10))


def func_final(x, y, func):
    print(x*y*func(10))


func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x*1000))
