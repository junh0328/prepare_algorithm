# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print("1:", len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print("2:", 'apple;orange;banana;lemon')

# 3. 화면에 * 기호 100개를 표시하세요.

print("3:", '*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

q4 = '30'
int_q4 = int(q4)
float_q4 = float(q4)
complex_q4 = complex(q4)

print(type(int(int_q4)), int_q4)
print(type(float(float_q4)), float_q4)
print(type(complex(complex_q4)), complex_q4)
print(type(q4), q4)

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

q5 = 'Niceman'

print(q5[4:len(q5)])
print("5:", q5.replace('Nice', ''))

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

sb = 'Strawberry'
list_sb = list(sb)
list_sb.reverse()
# print(list_sb)
print("6:", ''.join(list_sb))

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

phone = "010-7777-9999"
answer = []

for i in range(0, len(phone)):
    if(phone[i] != '-'):
        answer.append(phone[i])

print("7:", ''.join(answer))


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

url = "http://daum.net"

print('8:', url.replace('http://', ''))


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

m = "NicemMan"
answer = []

for i in range(0, len(m)):
    if(m[i].islower()):
        answer.append(m[i].upper())
    else:
        answer.append(m[i].lower())

print("9:", ''.join(answer))

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

print("10:", 'abcdefghijklmn'[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

Arrlist = ["Banana", "Apple", "Orange"]

del Arrlist[1]

print("11:", Arrlist)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

t = (1, 2, 3, 4)
print("12:", list(t))


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

dictObj = {
    "성인": -100000,
    "청소년": -70000,
    "아동": -30000
}

print("13:", type(dictObj), dictObj)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

dictObj['소아'] = -0

print("14:", dictObj)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print("15:", dictObj.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.

print("16:", dictObj.values())


# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
