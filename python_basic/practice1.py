print('과제 2---')
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(map(lambda x: str(int(x) + 1), a))
print(a)

# 나의 풀이
# 한 줄의 코드로 작성해야 하는데, 람다 함수를 바탕으로 두 줄로 만들었다

# a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# a = list(map(lambda string: str(int(string) + 1), a))

# print(a)

print()

print('과제 3---')
a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer',
     'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
for sport in set(a):
    print(sport, a.count(sport))


# 나의 풀이

# a = ['power ball', 'base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball',
#      'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']

# cnt_basket_ball = 0
# cnt_base_ball = 0
# cnt_soccer = 0

# for i in a:
#     if(i == 'basket ball'):
#         cnt_basket_ball += 1
#     elif(i == 'base ball'):
#         cnt_base_ball += 1
#     elif(i == 'soccer'):
#         cnt_soccer += 1
#     else:
#         continue

# print('basket ball', cnt_basket_ball)
# print('base ball', cnt_base_ball)
# print('soccer', cnt_soccer)
