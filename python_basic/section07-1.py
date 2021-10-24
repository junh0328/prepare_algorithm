# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이
# 클래스 형태로 코딩을 한뒤 변수화하여
# 인스턴스에 할당하고 메모리에 올려 이를 사용한다

# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간, 모든 자료형은 자신만의 네임스페이스를 가진다
# 클래스 변수 : 직접 사용 가능 (js의 정적 메서드와 동일), 객체 보다 먼저 생성 , 해당 클래스를 사용하는 전체가 공유
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후에 사용, 각각이 개인적으로 가짐

# 선언

# class 클래스명:
#     함수
#     함수1
#     함수2

# 예제 1

# 첫글자가 대문자로 시작하는 것을 원칙으로 함
# 단어와 단어 사이에는 대문자로 구분

# 초기화
class UserInfo:
    # ① 속성(프로퍼티), ② 메서드로 구분된다
    # 1. __init__ 을 통해 초기화를 헤야 한다
    #
    def __init__(self, name):
        self.name = name
        print('초기화!')

    def user_info_p(self):
        print("Name:", self.name)


# 네임스페이스

user1 = UserInfo('Lee')
print('self.name:', user1.name)
user1.user_info_p()

print()

user2 = UserInfo('Park')
print('self.name:', user2.name)
user2.user_info_p()

print('id:', id(user1))
print('id:', id(user2))

print()

print(user1.__dict__)
print(user2.__dict__)

print()

# 예제 2
# self의 이해


class Parent:
    # self 인자가 없을 경우, 인스턴스 생성 시에 사용할 수 없다
    def function1():
        print('non self function called!')

    # self가 있을 경우
    def function2(self):
        print(id(self))
        print('self function called!')


child = Parent()

# Parent.function1()
# >>> 인스턴스로 만들었을 경우 finction1() 메서드는 self 키워드가 없어 누구의 인스턴스인지 알 수 없다
# 따라서 self 가 없는 (자바스크립트에서의 정적 메서드) 클래스 메서드를 사용할 때는 클래스를 직접 호출하여 사용한다

Parent.function1()

child.function2()

print('---------------', Parent.function1)


print(id(child))

Parent.function2(child)

print()

# 예제 3
# 클래스 변수 (self x), 인스턴스 변수 (self o)


class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        # 클래스 변수는 self가 없기 때문에 클래스 명을 통해 직접 접근해야 한다
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print()

print(WareHouse.__dict__)
# ... 'stock_num': 3, 클래스 변수는 사용자 모두가 공유하기 때문에, init(초기화)한 멤버 수만큼 증가하여 3이 되었다
print('stock_num:', WareHouse.stock_num)  # >>> 3

print()

print(user1.name)
print(user2.name)
print(user3.name)

print()

# 🔥 중요 🔥
# 자기 네임 스페이스에 해당 변수가 없다면 클래스 네임스페이스에서 찾는다
# 클래스 네임스페이스에도 없다면 에러를 발생시킨다

print(user1.stock_num)  # 3
print(user2.stock_num)  # 3
print(user3.stock_num)  # 3

print()

# user1을 지울 경우
# 공통 클래스 변수인 stock에 할당된 값도 줄어들 것이다

del user1

print(user2.stock_num)  # 2
print(user3.stock_num)  # 2
