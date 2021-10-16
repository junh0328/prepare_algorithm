# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

# while 문 v1 < 11 때까지 반복

v1 = 1

while v1 < 11:
    print('v1 is :', v1)
    v1 += 1

print()

# for 문 0 - 9까지 반복
# range(n) 함수에 매개변수가 1개라면 0부터 n-1까지를 의미한다

for v2 in range(10):
    print('v2 is :', v2)
    v2 += 1

print()

# for 문 1 - 10까지 반복

for v3 in range(1, 11):
    print('v3 is :', v3)
    v3 += 1

# 1 ~ 100 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

# while 문 사용
print('1~ 100 : ', sum1)

# sum 함수 사용
print('1~ 100 : ', sum(range(1, 101)))

# sum 함수 사용, range 짝수 (n, m, k) n 부터 m-1까지 k만큼 건너 뛰어서
print('1 ~ 100 : ', sum(range(1, 101, 2)))


print()


# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리 (집합과 딕셔너리는 순서가 없지만 이렇게 순회 가능한 타입들은 반복이 가능하다는 의미이다)
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# 리스트

names = ["Kim", "Park", "cho", "Choi", "Yoo"]

for i in names:
    print("Yo are: ", i)

print()

# 문자열

word = "dreams"

for string in word:
    print("Word : ", string)

print()

# 딕셔너리

my_info = {
    "name": "Kim",
    "age": 13,
    "city": "Seoul"
}

# 기본 값은 key를 순회한다

for key in my_info:
    print("my_info :", key)

print()

# 값을 순회

for key in my_info.values():
    print("my_info :", key)

print()

# 키를 순회

for key in my_info.keys():
    print("my_info :", key)

print()

# 아이템 (key, value)를 순회

for key, value in my_info.items():
    print("my_info :", key, value)

print()

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

print()

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 46, 48]

for num in numbers:
    if num == 33:
        print("Found: 33!")
        break
    else:
        print("not found: 33...")

print()

# for - else 구문
# for 문 안에서 truthy한 값을 만나 break가 작동하지 않은 경우에는 else문에서 최종적으로 print 된다

for num in numbers:
    if num == 33:
        print("Found: 33!")
        break
    else:
        print("not found: 33...")
else:
    print("Not found 33......🥲")

print()

for num in numbers:
    if num == 40:
        print("Found: 40!")
        break
    else:
        print("not found: 40...")
else:
    print("Not found 40......🥲")

print()

# continue
# continue 문의 조건에 부합할 경우 continue 밑의 코드를 실행하지 않고 다음 조건으로 이동

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print('float이 아닙니다...', type(v), v)

print()

# 자료구조 변환

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
print(set(reversed(name)))
