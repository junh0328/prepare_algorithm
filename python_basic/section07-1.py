# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#     함수
#     함수1
#     함수2

# 예제 1

# 첫글자가 대문자로 시작하는 것을 원칙으로 함
# 단어와 단어 사이에는 대문자로 구분

class UserInfo:
    # 속성(프로퍼티), 메서드
    # __init__ 을 통해 초기화를 헤야 한다
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name:", self.name)


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
