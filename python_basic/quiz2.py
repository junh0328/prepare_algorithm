import csv

with open('./resource/a.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # print(type(reader))
    # print(dir(reader))

    for ele in reader:
        sum = []
        sum.append(ele)

    print(sum, type(sum))


# def int_sum(*args):
#     try:
#         for n in args:
#             sum += n
#     except:
#         print('error')
#     return sum


# print(int_sum('lee'))

# import datetime

# # 삽입 날짜 생성
# now = datetime.datetime.now()
# print('now:', now)

# class Foo:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("I am "+self.name)

#     def speak():
#         print("Foo's static method")

#     def changeNaem(self, newName):
#         self.name = newName


# class Bar(Foo):
#     def __inti__(self, name):
#         super().__init__(name)

#     def speak(self):
#         print('You are ' + self.name)


# Foo.speak()
# bar = Bar('John')
# bar.speak()

# foo = Foo('Park')

# print(foo.name)
# foo.changeNaem('Lee')

# print(foo.name)
