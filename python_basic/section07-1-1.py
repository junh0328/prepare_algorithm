# 초기화
class UserInfo:
    # ① 속성(프로퍼티), ② 메서드로 구분된다
    # 1. __init__ 을 통해 초기화를 헤야 한다
    # 2. 인스턴스 생성 시에, (매직 메서드) __init__이 실행된다!
    def __init__(self, name):
        self.name = name
        print(self.name, '으로 초기화!')

    def user_info_p(self):
        print("Name:", self.name)


user1 = UserInfo('junhee')
user2 = UserInfo('kim')

print(id(user1), ',', id(user2))

print(user1.__dict__)
print(user2.__dict__)
