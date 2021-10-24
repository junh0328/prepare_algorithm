class Median:

    def __init__(self):
        self.item = []

    def get_item(self, item):
        self.item.append(item)

    def clear(self):
        self.item = []

    def show_result(self):
        self.item.sort()

        if len(self.item) % 2 == 1:
            idx = 0
            idx = int(len(self.item)/2)
            print(self.item[idx])
        else:
            print((self.item[0] + self.item[-1])/2)


median = Median()
for x in range(10):  # 0 - 9 까지
    median.get_item(x)  # 차례대로 x 의 값을 저장하는 메서드
median.show_result()  # 중앙값을 출력하는 메서드. 입력받은 값이 짝수개이면, 중앙값 2개의 평균을 출력

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()

# def sort_result(arr: list):
#     arr.sort()
#     print(arr)


# def show_result(arr: list):
#     if len(arr) % 2 == 1:
#         idx = 0
#         idx = int(len(arr)/2)

#         print('홀수')
#         print(arr[idx])
#     else:
#         print('짝수')
#         print((arr[0] + arr[-1])/2)


# show_result([1, 2, 3, 4, 5, 6, 7])

# sort_result([3, 2, 4, 1, 5, 6, 8, -1, -6])
