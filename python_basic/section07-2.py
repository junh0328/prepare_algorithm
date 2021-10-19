# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 상속받을 경우 부모의 모든 속성, 메서드 사용 가능

# 라면 클래스를 만든다고 가정
# 속성(종류, 회사, 맛, 면 종류, 이름) : 부모


class Car:
  # 문자열로 무슨 클래스인지 적어주면 좋다
    """Parent Class"""

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        super().__init__(type, color)  # super() 부모에게 상속받은 type, color라는 의미
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name :%s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        super().__init__(type, color)  # super() 부모에게 상속받은 type, color라는 의미
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name :%s" % self.car_name

    # 자식 클래스에서도 부모와 같은 메서드를 선언할 경우
    def show(self):
        # 부모의 메서드도 다이렉트로 호출하고 싶을 경우에는 부모의 show 메서드를 super를 통해 선언해준다
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


model1 = BmwCar('520d', 'sedan', 'blue')

# 프로퍼티

print(model1.color)  # Super 부모로부터 옴
print(model1.type)  # Super 부모로부터 옴
print(model1.car_name)  # Sub 자식으로부터 옴

print()

# 메서드

print(model1.show())  # Super
print(model1.show_model())  # Sub

print()

print(model1.__dict__)
# >>> {'type': 'sedan', 'color': 'blue', 'car_name': '520d'}

# Method Overriding(오버라이딩) 올라타다

# 자식 클래스를 통해 인스턴스를 만들었을 때
# 부모에 있는 메서드(show)를 자식에서 동일한 이름(show)으로 선언할 경우 자식에 선언된 메서드로 '오버라이딩' 된다

model2 = BenzCar('220d', 'suv', 'black')

print(model1.show())  # Car Class "Show Method!"
print(model2.show())  # Car Info : 220d suv black

print()

# Parent Method Call

model3 = BenzCar('400d', 'suv', 'navy')
print(model3.show())

print()

# Inheritance info (상속 정보를 리스트 형태로 반환한다)
# mro() 메서드를 통해 상속의 정보를 확인할 수 있다

print(BmwCar.mro())

# >>> [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]

print(BenzCar.mro())

# >>> [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]

print()

# 예제 2
# 다중 상속


class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())

# [
# <class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>,
# <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>
# ]

# 다중 상속이 가능하나 너무나 복잡한 다중 상속은 코드를 구현하는데 어려움이 있을 수 있다

print()

print(A.mro())

# [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]
