class Parent:
    # self 인자가 없을 경우, 인스턴스 생성 시에 사용할 수 없다
    def function1():
        print('non self function called!')

    def function2(self):
        print('self function called!')


Parent.function1()

Parent().function2()

print()
print()


class Foo():
    bar = 'A'

    def __init__(self):
        self.bar = 'B'

    class Bar():
        bar = 'C'

        def __init__(self):
            self.bar = 'D'


print(Foo.bar)
print(Foo().bar)
print(Foo.Bar.bar)
print(Foo.Bar().bar)
