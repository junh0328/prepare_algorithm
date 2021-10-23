# Section08
# 파이썬 모듈과 패키지

# 모듈 - 미리 구성해놓은 함수, 프로퍼티들을 재사용하기 위해 모아놓는 파일 단위
# 패키지 - 모듈들의 모음

# 패키지 예제

# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1, 클래스 형태 내부에 함수가 있을 때
# 클래스를 불러와야 하는 경우 (ex: import Fibonacci)
# from 문을 통해 해당 클래스의 위치를 기입해줘야 한다! 🔥

# from math_pkg.fibonacci import Fibonacci

import builtins
import math_pkg.prints as p
import math_pkg.calculations as c

from math_pkg.fibonacci import Fibonacci
from math_pkg.fibonacci import Fibonacci as fb
from math_pkg.calculations import div as d

print("ex1 :", end='')
Fibonacci.fibo(300)

print()

print("ex2 :", Fibonacci.fibo2(400))
print("ex2 :", Fibonacci().title)

# 사용2, (클래스), * 로 모듈의 기능 전체를 가져오기, 권장 x, 메모리를 많이 먹는다

# from math_pkg.fibonaccit import *

print()

# 사용3, (클래스) alias 주기 (as = alias)
# 가독성을 위해 as 를 통해 import 하는 클래스의 이름을 줄임말로 사용할 수 있다

# from math_pkg.fibonaccit import Fibonacci as fb (린팅에 의해 위로 올라가기 때문에 주석처리)

print("ex3 :", fb.fibo2(400))
print("ex3 :", fb().title)

print()

# 사용4, (함수)
# 모듈 전체 불러오기 + alias 사용하기

# import math_pkg.calculations as c

print("ex4 :", c.add(10, 20))
print("ex4 :", c.mul(10, 20))
print("ex4 :", c.div(10, 20))

print()

# 사용5, (함수)
# 일부만 불러오기

# from math_pkg.calculations import div as d

print("ex5 :", int(d(100, 10)))

print()

# 사용6

# import math_pkg.prints as p

p.print1()
p.print2()

# 빌트인 내장 모듈 보기
print(dir(builtins))
