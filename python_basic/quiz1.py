# q6

# a = ['파', '이', '썬', '썬', '썬', '즐', '즐', '즐', '거', '운']

# last = None

# for elem in a:
#     if elem == last:
#         continue
#     print(elem, end="")
#     last = elem

# q7

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = lambda_mul = lambda num: num * num
# c = list()

# for element in a:
#     c.append(b(element))
# print(c)

# >>> [0,1,4,9,16,25,36,49,64,81]

# 과제 2

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# lambda_plus = lambda string: str(int(string) +1)


def lambda_plus(string): return str(int(string) + 1)


a = list(map(lambda_plus, a))

print(a)
