# Section14-1
# 파이썬 심화
# 객체 참조 중요한 특징들

# Python Object Reference

import copy  # Deep Copy를 위해 사용할 copy 모듈

print('EX1-1 -')
print(dir())  # directory, 현재 스코프에 위치한 환경을 보여줌

print()

# id vs __eq__ (== 같다 표시) 증명
# 객체 비교

x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y))
# >>> EX2-1 - 4335567680 4335567680

print('EX2-1 -', id(x.get('name')), id(y.get('name')))
# >>> EX2-1 - 4502354544 4502354544

# why?
# 객체의 경우 불변성의 특징을 가지는 원시 타입과 달리, 변하는 가변성의 성질을 가지고 있다.
# 만약 객체가 참조하는 메모리의 주소가 아닌 실제 값을 가지고 있다면, 객체 내부의 값이 변할 때마다 재할당해야 하므로 비용이 많이 든다

# 따라서 객체는 얕은 복사(shallow)를 통해 id 값에 메모리 주소를 참조하고 있다.
# 만약 같은 메모리 주소를 참조하고 있는 객체 내부의 데이터를 변경하면 어떻게 될까?

x['name'] = 'lee'

# 객체는 객체를 할당한 변수(x)가 기억하는 메모리 주소를 통해 메모리 공간에 접근하여 참조 값에 접근할 수 있다.
# 객체는 변경 불가능한 값이 아니므로, 재할당하지 않더라도 객체를 직접 변경할 수 있다.
# 객체를 삽입 수정 삭제 하더라도 메모리 주소가 변경되지 않는다는 것을 의미한다

print('EX2-2 -', 'x:', x, 'y:', y)
# >>> EX2-2 - x: {'name': 'lee', 'age': 33, 'city': 'Seoul'} y: {'name': 'lee', 'age': 33, 'city': 'Seoul'}
print('EX2-2 -', id(x), id(y))
# >>> EX2-2 - 4417651520 4417651520 , 앞서 EX2-1에서 확인했던 x,y의 id값 즉 메모리 주소가 변경되지 않았음을 알 수 있다

# 원시 타입에 대해 생각해보자
# 원시 타입의 경우 불변성(변하지 않는 성질)을 가진다
# 따라서 한번 선언된 기존 메모리에 존재하는 값을 변경할 수 없기 때문에, 재할당을 통해 새로운 주소에 값을 할당한다

str1 = 'lee'
str2 = str1

print('EX2-3 -', id(str1), id(str2))
# EX2-3 - 4320787440 4320787440

# str1에 'kim'이라는 문자열을 재할당한다면 str2도 'kim'을 참조할까?
# 객체와 같은 구조(가변성)라면 같은 주소를 가리키고 것이다
str1 = 'kim'

print('EX2-4 -', str1, str2)
print('EX2-4 -', id(str1), id(str2))
# EX2-4 - kim lee
# EX2-4 - 4376099440 4376345584

# 아니다, 문자열과 같은 원시 값의 경우 변경 불가능한 값이기 때문에 값을 직접 변경할 수 없다.
# 따라서 변수 값을 변경하기 위해 원시 값을 재할당(kim) 하면, 새로운 메모리 공간을 확보하고 재할당한 값을 저장한다
# 그렇기 때문에 참조하던 메모리 공간의 주소(id)가 변경된다 4320787440 > 4376345584

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__)는 값을 비교한다

print()
print()

# 튜플 불변형의 비교 (파이썬의 튜플은 불변성의 성질을 갖는다.)

tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
# >>> EX3-1 - 4361677760 4361677504
print('EX3-2 -', tuple1 is tuple2)  # 객체 주소(id) 비교
# >>> EX3-2 - False
print('EX3-3 -', tuple1 == tuple2)  # 값 비교
# >>> EX3-3 - True
print('EX3-4 -', tuple1.__eq__(tuple2))
# >>> EX3-4 - True

print()
print()

# Copy, Deepcopy(얕은 복사, 깊은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-2 -', tl1 is tl3)

# EX4-1 - True
# EX4-2 - True
# EX4-3 - True
# EX4-2 - False

print()

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)
print('external:', id(tl1[2]))

print()

tl1[1] += [110, 120]
tl1[2] += (110, 120)


print('EX4-8 -', tl1)
print('EX4-9 -', tl2)  # 튜플 재 할당(객체가 새로 생성됨, 메모리 주소가 변경됨)
print('EX4-10 -', tl3)
print('after:', id(tl1[2]))

print()
print()

# Deep Copy

# 장바구니


class Basket():
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)

# import copy


basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)      # 복사
basket3 = copy.deepcopy(basket1)  # 깊은 복사

print('EX5-1 -', id(basket1), id(basket2), id(basket3))
# >>> EX5-1 - 4318378352 4318377392 4318368128

print('EX5-2 -', id(basket1._products),
      id(basket2._products), id(basket3._products))
# >>> EX5-2 - 4345866816 4345866816 4345866688

# deep copy로 복사하지 않을 경우, 내부의 가리키는 데이터의 주소가 동일하다
# 그말인 즉, basket1의 Item을 변경하면, basket2의 Item이 변경될 수 있다는 의미이다
# 따라서 깊은 복사를 통해 객체가 동일한 메모리 주소를 참조하지 않도록 만들어줘야 한다

print()

# 증명
# 첫 번째 바구니는 오렌지를 넣고, 두 번째 바구니는 Snack을 빼고 싶은 경우

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)

print()
print()

# 함수 매개변수 전달 사용법


def mul(x, y):
    x += y
    return x


x = 10
y = 5


print('EX6-1 -', mul(10, 5), x, y)
# >>> EX6-1 - 15 10 5
print()

a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b)  # 가변형 a -> 원본 데이터 변경
# >>> EX6-2 - [10, 100, 5, 10] [10, 100, 5, 10] [5, 10]
# 원본 데이터 리스트 a 또한 변경된 상황

c = (10, 100)
d = (5, 10)

print('EX6-3 -', mul(c, d), c, d)  # 불변형 c -> 원본 데이터 변경 x
# >>> EX6-3 - (10, 100, 5, 10) (10, 100) (5, 10)

print()
print()

# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 x -> 참조 반환
# 어떻게 복사를 하던 하나의 id 값을 갖는다

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt1 is tt3, id(tt1), id(tt3))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'
ss3 = ss1


print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
print('EX7-5 -', ss1 is ss3, ss1 == ss3, id(ss1), id(ss3))

ss1 = 'Orange'

print('EX7-6 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
print('EX7-7 -', ss1 is ss3, ss1 == ss3, id(ss1), id(ss3))
