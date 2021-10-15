# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서 x, 중복 x, 수정 o, 삭제 o

# Key, Value (Json) 로 이루어진 형식

# 딕셔너리 선언

a = {
    'name': 'junhee',
    'phone': '010-7777-7777',
    'birth': 970328
}

b = {
    0: 'Hello Python',
    1: 'Hello Coding'
}

c = {
    'arr': [1, 2, 3, 4, 5],
    'tuple': (1, 2, 3, 4, 5)
}

print(type(a))  # >>> <class 'dict'>

print()

# 딕셔너리 출력

# 직접 접근하기
print(a['name'])

# get을 통해 접근하기
# 있을 경우 직접 접근과 동일하게 출력
print(a.get('name'))

# 없을 경우에는 Error 대신 None 출력 >>> 따라서 안전하게 조회할 수 있다 (에러 핸들링이 가능하다)
print(a.get('address'))

print(c['arr'][1:3])  # [2, 3]

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
# {'name': 'junhee', 'phone': '010-7777-7777', 'birth': 970328, 'address': 'Seoul'}


a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3, 4)

print(a)
# {'name': 'junhee', 'phone': '010-7777-7777', 'birth': 970328, 'address': 'Seoul', 'rank': [1, 3, 4], 'rank2': (1, 2, 3, 4)}

print()

# keys, values, items

# key

# 딕셔너리 a의 key 값만 가져오고 싶을 때
print(a.keys())
# >>> dict_keys(['name', 'phone', 'birth', 'address', 'rank', 'rank2'])

# 배열의 형태가 아니기 때문에 인덱싱으로 접근할 수 없다
# print(a.keys()[0])  # Error: 'dict_keys' object is not subscriptable

# 따라서 배열로 형변환을 한다면 그 후에 접근이 가능해진다
print(list(a.keys())[0])
print(list(a.keys()))

print()

# value

print(a.values())
print(list(a.values()))
print(list(a.values())[:len(list(a.values()))])

print()

# item

# 배열안에 각 key, value 의 쌍으로 이루어진 튜플이 들어있는 형식으로 반환된다

print(a.items())
print(list(a.items()))

# [
#     ('name', 'junhee'),
#     ('phone', '010-7777-7777'),
#     ('birth', 970328),
#     ('address', 'Seoul'),
#     ('rank', [1, 3, 4]),
#     ('rank2', (1, 2, 3, 4))
# ]

print()

# 집합(Sets) (순서 x, 중복 x, 추가 o, 제거 o)

# 집합 선언

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)  # 중복을 허용하지 않기 때문에 알아서 제거되어 나옵니다  {1, 4, 5, 6}

# 중복을 제거한 상태에서 집합 또는 튜플로 변환하여 주로 사용한다

t = tuple(b)
print(t)
l = list(b)
print(l)

# 집합 함수 사용

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합

print(s1.intersection(s2))
print(s1 & s2)

# {4, 5, 6}

print()

# 합집합

print(s1.union(s2))
print(s1 | s2)

# {1, 2, 3, 4, 5, 6, 7, 8, 9}

print()

# 차집합

print(s1.difference(s2))
print(s1 - s2)

# {1, 2, 3}

print()

# 집합(Sets) 추가 & 제거

s3 = set([7, 8, 10, 15])

print(s3)

# 추가

s3.add(18)
print(s3)

# 제거

s3.remove(15)
print(s3)

print(type(s3))

# >>> <class 'set'>
