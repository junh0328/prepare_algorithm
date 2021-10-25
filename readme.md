# 제로베이스 알고리즘 자료구조 51일 대비반 👨🏻‍💻

## 2021.10.12, day 01

### ① Mac OS 환경 설정 및 세팅

현재 경로에서 해당 bin(binary) 폴더로 이동

```bash
$ cd python_basic/bin
```

가상 서버 활성화

```bash
$ source ./activate
```

### ② print() 함수 배우기

- 가장 기본적인 Output(출력) 함수
- 기본 출력
- Separator, End 옵션 사용
- Format 형식 출력
- Escape Code 사용법

### print 함수 특징

**'', "" 를 구분하지 않는다**

```python
print('hello world!')
print("hello world!")
print("""hello world!""")
print('''hello world!''')
```

**Separator 옵션을 통해 입력한 문자열을 합칠 수 있다**

[Array.prototype.join() 🔥](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/join) 과 같은 기능을 한다

```python
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')
```

**end 옵션을 사용 (끝을 내지 않겠다)**

end 옵션을 통해 각 줄별로 입력한 문자열을 이어줄 수 있다

```python
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
```

## 2021.10.13, day 02

### ① print() 함수 배우기 2

- Format 형식 출력
- Escape Code 사용법

```py
# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
```

```py
# index처럼 0 , 1 각 자리에 위치한 문자열을 매핑(할당)한다 >> You and Me and You
print('{0} and {1} and {0}'.format('You', 'Me'))
```

```py
# 매개변수에 값을 넣어주는 형태로 더욱 직관적으로 사용할 수 있다. >> You and Me
print("{a} are {b}".format(a='You', b='Me'))
```

```py
# format 함수를 쓰고 싶지 않고, 문자열 또는 정수, 실수를 나타내고 싶다면? 아래와 같은 방법으로 사용 가능하다
# 튜플 형태 ( , ) 로 format 형태를 대신하여 적을 수 있다

# %s: 문자, %d: 정수, %f: 실수

print("%s's favorite number is %d" % ('junhee', 7))
```

```py
# %와 문자 또는 숫자를 나타내는 [ s, d, f ] 사이에 숫자를 넣으면, 최대 자릿수를 정해줄 수 있다
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))
```

```py
# print() 시에 'you'를 표현하고 싶은 경우 쌍이 맞거나, 이스케이프 코드를 사용할 수 있다
print("'You'")
print('\'You\'')
print('"You"')
print("""'You'""")
print('\\yout\\\n') # 다르다
print('test')
print('\t tab 2')
```

### Escape Code

```py
# 참고 : Escape 코드

"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
"""
```

### ② 파이썬 구성요소 기초 학습

- 인코딩
- 변수
- 조건문
- 함수, 클래스, 인스턴스(객체)
- 정보 출력

```py
# import this
import sys

# 파이썬 기본 인코딩
print('입력:', sys.stdin.encoding)
print('출력:', sys.stdout.encoding)

# 출력문
print('My name is Junhee Lee')

# 변수 선언
MyName = 'Junhee'

print('Hello', MyName)

# 조건문
if MyName == 'Junhee':
    print('OK,', MyName, 'is right veriable')  # indent, 들여쓰기

# 반복문

for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i * j)


# 변수 선언(한글), 가능하지만 쓰지 않는 것을 추천
이름 = '준희'

# 출력
print('Hello', 이름)

# 함수 선언


def 인사(a):
    print('안녕하세요.', a, '님 반갑습니다!')


def greeting():
    print('Hello!')


# 함수 호출
인사('준희')
greeting()

# 클래스


class Cookie:
    pass


# 객체 생성
cookie = Cookie()

# 정보 값 출력
# id, dir은 사용자 정의 함수가 아닌 제공되는 빌트인 메서드이다
print(id(cookie))
print(dir(cookie))
```

### ③ 파이썬 가상환경

**별개의 가상환경을 사용한다면 해당 가상 환경을 통해서 여러개의 다양한 버전의 파이썬과 모듈을 사용하더라도, 효과적으로 관리가 가능해진다**

- 원하는 패키지만을 설치하여, 깔끔한 환경을 구성할 수 있다.
- 가상환경 별로 미리 작성된 코드를 활용하여 빠르게 프로토타이핑 할 수 있다.
- 특정 버전의 패키지를 설치하여 테스트해 볼 수 있다.

<img src="./images/1.png" alt="가상환경 필요성">

### 파이썬 가상환경 명령어 기초

- 가상환경 생성
- 가상환경 실행 / 해제
- 패키지 설치 및 삭제
- 패키지 리스트 출력
- 패키지 검색

**① 가상환경 생성**

해당 환경의 상위 디렉토리 예를 들어 📁FastCampus/python_basic 이라는 경로에 가상환경을 설정하고 싶은 경우

FastCampus에서 아래와 같은 명령어를 통해 가상환경을 생성한다

```
// venv : virtual environment, 가상 환경을 의미한다
$ python3 -m venv python_basic
```

**② 가상황경 실행 / 해제**

후에 생성된 📁FastCampus/python_basic/bin 으로 접근한다

```
📁 bin (binary) 폴더 내부에 있는 파일이자 명령어인 activate를 실행한다

$ source ./activate
```

```
$ source ./deactivate
```

**③ 패키지 설치 및 삭제**

```
$ pip install simplejson

$ pip uninstall simplejson
```

**④ 패키지 리스트 출력**

```
$ pip list
```

**⑤ 패키지 검색**

```
$ pip search simplejson
```

pip search 시에 오류가 날 경우, 해당 사이트에서 직접 검색 후에 다운이 가능하다

```
https://pypi.org/
```

<details>
<summary>그 외의 다양한 명령어 보기</summary>

```python
'''
python -m venv 가상환경명
	Script\activate.bat
	Script\deactivate.bat
	pip 명령어 : search , install, uninstall, list, freeze, show
	pip install search simplejson , simple*
	pip install install simplejson
	pip install install simplejson==버전
	pip install --upgrade simplejson
	pip show simplejson
	pip show -f simplejson
	pip freeze > packages.txt
	pip freeze --all > packages.txt
	pip install -r packages.txt


	python -m venv /path/to/venv : 윈도우, 맥, 리눅스 동일

	윈도우 : Script
	맥 : bin

	윈도우

	activate.bat : 가상환경 진입
	deactivate.bat : 가상환경 해제

	맥
	source ./activate : 가상환경 진입
	source ./deactivate : 가상환경 해제

	command : code 실행
'''
```

</details>

## 2021.10.14, day 03

### python data type (파이썬 데이터 타입 종류)

- Boolean
- Numbers
- String
- Bytes
- Lists
- Tuples
- Sets
- Dictionaries

### Boolean

```py
v_bool = True  # False, 첫 문자는 대문자로 작성해야 한다

print(type(v_bool))
```

```
>>>
<class 'bool'>
```

### Numbers

```py
v_int = 7
v_float = 10.2

print(type(v_int))
print(type(v_float))
```

```
>>>
<class 'int'>
<class 'float'>
```

### String

```py
v_str= 'Goody Boy'

print(type(v_str))
```

```
>>>
<class 'str'>
```

### Bytes

### Lists

```py
v_list = [3, 5, 6] # 다른 언어(js)에서는 배열이라고도 한다

print(type(v_list))
```

```
>>>
<class 'list'>
```

### Tuples

```py
v_tuple = 3, 5, 7

print(type(v_tuple))
```

```
>>>
<class 'tuple'>
```

### Dictionaries

```py
v_dict = {
	"name": "Junhee",
	"age": 25
}

print(type(v_dict))
```

```
>>>
<class 'dict'>
```

### ① 파이썬 숫자형(Numbers) 및 연산자

- `+` : 더하기
- `-` : 빼기
- `*` : 곱하기
- `/` : 나누기
- `//` : 나누기 (몫)
- `%` : 나누기 (나머지)
- `**` : 지수연산 (제곱)
- 단항 연산자

### 파이썬 숫자형 및 연산자 사용하기

```py
i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5  # 0.5
f4 = 10.  # 10.0

print()

print(i1*i2)
print(f1 ** f2)
print(f3+i2)  # 결과값이 실수기 때문에 자동으로 형변환이 된다!

print()

result = f3 + i2
print(result, type(result))

# float 과 int를 연산할 때

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a+b
print(result2)

# 형 변환
# int, float, boolean, complex(복소수)

print(int(result2))  # float > int
print(float(c))  # int > float
print(complex(3))
print(int(True))  # 1로 변환
print(int(False))  # 0으로 변환
print(int('3'), type(int('3')))  # 문자열을 정수로 변환

y = 100
print('before y:', y)
y += 100

print('after y:', y)

# 수치 연산 함수

print('abs:', abs(-7))  # 절대값 absolute
n, m = divmod(100, 8)  # 몫은 n으로 나머지는 m으로 보내주는 함수
print(n, m)

# math 모듈이 제공하는 정적 메서드
print(math.ceil(5.1))  # 올림
print(math.floor(3.74))  # 버림
print(math.pi)  # 파이값 출력
```

### ② 파이썬 문자형 관련 연산자

- 문자열 생성, 길이
- 이스케이프 문자
- 문자열 연산
- 문자열 형 변환
- 문자열 함수
- 문자열 슬라이싱

### 문자열 생성, 길이

```py
str1 = "I'm a boy"
str2 = 'Nice man'
str3 = ''
str4 = str('')

print(len(str1), len(str2), len(str3), len(str4))
```

### 이스케이프 문자

```py
escape_str1 = "Do you have a \"big collection?\""
escape_str2 = 'Do you have a "big collection?"'
escape_str3 = 'Tab\tTab\tTab'

print(escape_str1)
print(escape_str2)
print(escape_str3)
```

#### Raw String

```py
# Raw String: r'' / r"" 작은 따옴표 또는 큰 따옴표 내부에 있는 이스케이프 처리는 이스케이프 처리가 되지 않고 그대로 출력된다

raw_s1 = r'C:\Programs\Test\Bin'
raw_s2 = r"\\a\\a"

print(raw_s1)
print(raw_s2)
```

#### 멀티라인

```py
# 멀티라인: 변수 선언 이후에 '\' 기호가 나온다면 문자열을 enter키를 포함하여 다음줄에 나온다는 것을 의미한다
multi = \
    """
문자열

멀티라인

테스트
"""
print(multi)
```

### 문자열 연산

```py
# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'NiceMan'

print(str_o1 * 10)
print(str_o2 + str_o3)
print(str_o1 * 3)

# 한쪽만 문자열일 경우에는 * 연산자를 만나 형변환을 하지만 * 연산자의 좌항과 우항이 모두 문자열일 경우에는 에러가 난다

# print('a' * 'a') 좌항 우항 모두 문자열
# print(str_o1 * '3') 좌항 우항 모두 문자열 > TypeError: can't multiply sequence by non-int of type 'str'
```

#### in 연산자

```py
print('a' in str_o4)  # True, str_o4 안에 'a' 라는 문자열이 있니?
print('m' in str_o4)  # False, 대소문자를 구분한다
print('m' not in str_o4)  # True, str_o4 안에 'm' 이라는 문자열이 없니?
```

### 문자열 형 변환

```py
print(str(77))  # 숫자를 str()로 하여금 문자열로 변환함
print(str(77) + 'a')  # 결론적으로 문자 + 문자가 가능하게 됨
print(str(10.4))
```

### 문자열 함수

```py
a = 'niceman'
b = 'orange'

print(a.islower())  # a 문자열이 소문자로 되어 있니?
print(a.endswith('n'))  # a 문자열의 끝 글자가 n으로 끝나니?
print(a.capitalize())  # Niceman > 첫 글자만 대문자로 변경
print(a.replace('nice', 'holy'))  # 첫 번째 파라미터에 들어온 문자열을 두 번째 파라미터에 들어온 문자열로 대체

# 리스트 함수

print(list(b))  # b 문자열을 리스트 형으로 변환 ['o', 'r', 'a', 'n', 'g', 'e']
print(list(reversed(b)))  # b 문자열을 리스트 형으로 변환한 후 뒤집음(reversed)
```

### 문자열 슬라이싱

문자열의 범위를 지정한다 (일부분을 추출한다)

```py
a = '01234567'

print(a[0:3])  # 문자열 a의 0번째 인덱스부터 3번째 인덱스 전까지 (n-1) 까지 나와라 >>> 012
print(a[0:4])  # >>> 0123
print(a[0:len(a)])  # 0부터 문자열 a의 길이 (7) 전까지 나와라
print(a[:4])  # 처음부터 4번째 인덱스 전까지 (n-1) 까지 나와라 >>> 0123
print(a[:])  # 전체 다 나와라
print(a[0:len(a):2])  # 0부터 끝까지 나오는데, 2만큼 건너뛰고 나와라 >> 0246
print(a[0:-2])  # 0부터 (뒤에서부터 -2) 전까지 012345
print(a[::-1])  # 거꾸로 다 나와라 76543210
print(a[::2])  # 0부터 끝까지 2만큼 건너뛰고 나와라 >> 0246
```

### 파이썬 자료구조(List, Tuple)

- 리스트 특징
- 튜플 특징
- 인덱싱
- 슬라이싱
- 삽입, 삭제, 함수 사용

### 리스트 특징

- 순서 o
- 중복 o
- 수정 o
- 삭제 o

### 리스트 선언

```py
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]
```

### 리스트 인덱싱

Banana를 추출하고 싶을 때

```py
print(d[3])  # 인덱스 3에 위치한 요소 추출
print(d[-2])  # 뒤에서부터 -2번째 요소 추출
print(e[2][1])  # 2차원 베열 내부에서 인덱스 1에 위치한 요소 추출
print(e[2][-2])  # 2차원 배열 내부에서 뒤에서부터 -2번째 요소 추출
```

### 리스트 슬라이싱

```py
# 범위를 지정한다 (일부분을 추출한다)
print(d[0:3])  # 인덱스 0 부터 인덱스 3 전까지 (2 까지)
print(e[2][1:3])  # 2차원 배열의 인덱스 1부터 3전까지 (2까지)
print(e[2][1:len(e[2])])  # 2차원 배열의 인덱스 1부터 e[2]의 길이 전까지 >>> len(e[2]) = 3
```

## 2021.10.15, day 04

### 리스트 연산

```py
print(c + d)
print(c*3)
# print(c[0] + 'hi') error, number + string의 식은 자동 형변환이 불가능하다
print(str(c[0]) + 'hi')
```

### 리스트 수정, 삭제

```py
c[0] = 77
print(c)

# 슬라이싱 후 대입 기존 리스트의 구간보다 대입하는 구간의 길이가 길다면 리스트의 길이가 늘어난다 (삽입으로 인해)
c[1:2] = [100, 1000, 10000]
print(c)  # [77, 100, 1000, 10000, 3, 4]


c[1] = ['a', 'b', 'c']
print(c)  # [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

del c[1]
print(c)  # [77, 1000, 10000, 3, 4]

del c[-1]
print(c)  # [77, 1000, 10000, 3]
```

### 리스트 함수

```py
y = [5, 2, 3, 1, 4]
print(y)

y.append(6)  # push와 같음, 배열의 끝 부분에 해당 요소를 추가한다
print(y)  # [5, 2, 3, 1, 4, 6]

y.sort()  # 오름차 순으로 배열을 정리한다
print(y)  # [1,2,3,4,5,6]

y.reverse()  # 배열을 뒤집어서 반환한다
print(y)  # [6,5,4,3,2,1]

y.insert(2, 7)  # 배열에 인덱스 n 뒤에 m 요소를 삽입한다. (n, m) 인덱스 n 자리에 m 요소를 삽입한다
print(y)  # [6, 5, 7, 4, 3, 2, 1]

y.remove(2)  # 배열에서 요소 m 이 있다면 해당 요소를 삭제한다
print(y)  # [6, 5, 7, 4, 3, 1]

y.pop()  # 배열의 맨 마지막 요소를 제거한다
print(y)  # [6, 5, 7, 4, 3]

ex = [88, 77]
y.extend(ex)  # 배열의 맨 마지막에 해당 변수를 넣어 확장한다
print(y)  # [6, 5, 7, 4, 3, 88, 77]

# 추가(삽입) : append, insert, extend
# 삭제 : del, remove, pop
```

### 튜플 특징

- 순서 o
- 중복 o
- 수정 x
- 삭제 x

### 튜플 선언

튜플 선언 (리스트와 달리 소괄호로 선언한다)

```py
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
```

### 튜플 참조 (인덱싱)

```py
# 튜플 참조 리스트와 같이 [ ] 대괄호를 사용하여 참조한다

print(c[2])
print(c[3])
print(d[2][2])

# del c[2]: 'tuple' object doesn't support item deletion >> 튜플은 수정과 삭제가 되지 않는다
```

### 튜플 슬라이싱

```py
print(d[2:])
print(d[2][0:2])

# 삽입이 가능하나, 수정, 삭제가 불가능하므로 신중히 진행해야 한다
print(c+d)
print(c*3)
```

### 튜플 함수

```py
z = (5, 2, 1, 3, 4, 1)

print(z)
print(3 in z)
print(6 not in z)
print(z.index(3))  # 튜플에서 해당 요소가 위치하고 있는 인덱스를 반환합니다
print(z.count(1))  # 튜플에서 해당 요소의 개수를 반환합니다
```

### 파이썬 자료구조(Dictonary, Set)

- 딕셔너리 특징
- 딕셔너리 추가
- 집합 특징
- 집합 자료형 함수
- 자료형 변환

### 딕셔너리 (Dictonary)

### 딕셔너리 특징

- 순서 x
- 중복 x
- 수정 o
- 삭제 o

딕셔너리는 Key, Value (Json) 로 이루어진 형식이다

#### 딕셔너리 선언

```py
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
```

### 딕셔너리 출력

```py
# 직접 접근하기
print(a['name'])

# get을 통해 접근하기
# 있을 경우 직접 접근과 동일하게 출력
print(a.get('name'))

# 없을 경우에는 Error 대신 None 출력 >>> 따라서 안전하게 조회할 수 있다 (에러 핸들링이 가능하다)
print(a.get('address'))

print(c['arr'][1:3])  # [2, 3]
```

### 딕셔너리 추가

```py

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
```

### 집합 특징

- 순서 x
- 중복 x
- 추가 o
- 제거 o

### 집합 선언

```py
# 집합 선언

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a)) # >>> <class 'set'>
print(c)  # 중복을 허용하지 않기 때문에 알아서 제거되어 나옵니다  {1, 4, 5, 6}

# 중복을 제거한 상태에서 집합 또는 튜플로 변환하여 주로 사용한다

t = tuple(b)
print(t)
l = list(b)
print(l)
```

### 집합 자료형 함수

```py
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
```

### 퀴즈 개인 답안

```py
# Section04-5

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
```

### 느낀점

파이썬 코드 작성시에 변수를 빌트인 객체와 같이 줘도 문제가 없어서 계속 str, list, obj 이런식으로 변수명을 선언했다가 출력할 때 에러가 생겼다

자율성이 부여되는 만큼 나만의 규칙을 정하고 변수명을 지어야겠다!

`#6, #7, #9` 번은 이런식으로 풀라고 내주신 문제가 아닌 것 같은데 기존 js 문제를 풀던 생각대로 풀다보니 이렇게 풀게 되었다

정답은 같겠지만, 선생님의 풀이를 듣고 만약에 다른 것이 있다면 추가적으로 공부해야 겠다

<details>
<summary>선생님 풀이 보기</summary>

```py
# 1. 아래 문자열의 길이를 구해보세요.
import re
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print("1. ", len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
# apple;orange;banana;lemon

print("2. ", "apple;orange;banana;lemon")

# 3. 화면에 * 기호 100개를 표시하세요.

print('3. ', '*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

print('4. ', int('30'))
print('4. ', float('30'))
print('4. ', complex('30'))
print('4. ', str(30))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

q5 = 'Niceman'
q5_idx = q5.index('man')

print('5. ', q5[q5_idx:])
print('5. ', q5[q5_idx: q5_idx+3])
print("5. ", q5[4:7])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry" 🔥 까먹었던 것

q6 = "Strawberry"

print('6. ', ''.join(list(reversed(q6))))
print('6. ', q6[::-1])  # 🔥 까먹었던 것

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999" # 🔥 까먹었던 것

q7 = "010-7777-9999"

print("7. ", q7[0:3] + q7[4:8] + q7[9:])  # 🔥 까먹었던 것
print("7. ", q7[0:3] + q7[4:8] + q7[9:13])

# 정규 표현식 (regex, regular expression)

# import re

print("7. ", re.sub('[^0-9]', '', q7))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

q8 = "http://daum.net"

print("8. ", q8[7:])


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
# 🔥 대문자/ 소문자를 대문자를 소문자로 소문자를 대문자로 라고 잘못 이해함

print("9. ", "Niceman".upper())
print("9. ", "Niceman".lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

q10 = "abcdefghijklmn"

print("10. ", q10[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"] 🔥 remove 함수 사용

q11 = ["Banana", "Apple", "Orange"]

q11.remove("Apple")  # 🔥 remove 함수 사용

print("11. ", q11)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

q12 = (1, 2, 3, 4)
print("12. ", list(q12))

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

q13_dict = {
    '성인': 100000,
    '청소년': 70000,
    '아동': 30000
}

q13_dict_2 = {}
q13_dict_2['성인'] = 100000
q13_dict_2['청소년'] = 70000
q13_dict_2['아동'] = 30000

print("13. ", q13_dict)
print("13. ", q13_dict_2)


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

q13_dict['소아'] = 0

print("14. ", q13_dict)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print("15. ", q13_dict.keys())
print("15. ", list(q13_dict.keys()))

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.

print("16. ", q13_dict.values())
print("16. ", list(q13_dict.values()))

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***

```

</details>

## 2021.10.16, day 05

### IF(조건문)

- 조건문 기본 형식
- 관계 연산자 실습(>, >=, <, <=, ==, !=)
- 논리 연산자 실습(and, or, not)
- 다중 조건문 (if, elif, else)
- 중첩 조건문

### 조건문 기본 형식

```py
# 예1
if True:
    print('참 입니다!')

# 예2
if False:
    print('거짓 입니다')
else:
    print('참 입니다!')
```

### 관계 연산자 실습

```py
# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 참 거짓 종류 (True, False)

# 참 : '내용', [내용], (내용), {내용}, 1 >>> 내용이 있는 자료형
# 거짓 : '', [], (), {}, 0 >>> 내용이 없는 자료형

city = ''

if(city):
    print(city)
else:
    print('city가 빈 문자열입니다')
```

### 논리 연산자 실습

```py
# and, or, not 문자 그대로 사용

a = 100
b = 60
c = 15

print('and: ', a > b and b > c)
print('or: ', a > b or c > b)  # 둘 중 하나만 만족하더라도 true
print('not:', not a > b)
print('"not False:" ', not False)
print('"Ænot True:" ', not True)

print()
```

### 산술, 관계, 논리 연산자

```py
# 산술 > 관계 > 논리 순서로 적용 (우선순위)

print('ex1 :', 5+10 > 0 and 7 + 3 == 10)

score1 = 90
score2 = 'A'


if score1 >= 90 and score2 == 'A':
    print('합격')
else:
    print('불합격입니다')
```

### 다중 조건문

```py
num = 2

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print('num 등급 D, 탈락', num)

print()
```

### 중첩 조건문

```py
# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print('A지망 지원 가능')
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

```

### For, while (반복문)

- 파이썬 코딩의 핵심
- 시퀀스 타입 반복
- Continue, Break
- For - else 구문
- 자료구조 변환

### 기본 반복문 : for, while

### while 문 >>> 조건이 true가 될 때까지 반복

```py
# while 문 v1 < 11 때까지 반복

v1 = 1

while v1 < 11:
    print('v1 is :', v1)
    v1 += 1
```

### for 문

```py
# for 문 0 - 9까지 반복
# range(n) 함수에 매개변수가 1개라면 0부터 n-1 까지를 의미한다

for v2 in range(10):
    print('v2 is :', v2)
    v2 += 1

print()

# for 문 1 - 10까지 반복

for v3 in range(1, 11):
    print('v3 is :', v3)
    v3 += 1
```

### 시퀀스 타입 반복

```py
# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리 (집합과 딕셔너리는 순서가 없지만 이렇게 순회 가능한 타입들은 반복이 가능하다는 의미이다)
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# 리스트

names = ["Kim", "Park", "cho", "Choi", "Yoo"]

for i in names:
    print("Yo are: ", i)

# 문자열

word = "dreams"

for string in word:
    print("Word : ", string)

# 딕셔너리

my_info = {
    "name": "Kim",
    "age": 13,
    "city": "Seoul"
}

# 기본 값은 key를 순회한다

for key in my_info:
    print("my_info :", key)

# 값을 순회

for key in my_info.values():
    print("my_info :", key)

# 키를 순회

for key in my_info.keys():
    print("my_info :", key)

# 아이템 (key, value)를 순회

for key, value in my_info.items():
    print("my_info :", key, value)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())
```

### break 문

```py
# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 46, 48]

for num in numbers:
    if num == 33:
        print("Found: 33!")
        break
    else:
        print("not found: 33...")
```

### break문, for - else 구문

```py
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
```

### continue 문

```py
# continue
# continue 문의 조건에 부합할 경우 continue 밑의 코드를 실행하지 않고 다음 조건으로 이동

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print('float이 아닙니다...', type(v), v)

print()
```

```
>>>
float이 아닙니다... <class 'str'> 1
float이 아닙니다... <class 'int'> 2
float이 아닙니다... <class 'int'> 5
float이 아닙니다... <class 'bool'> True
float이 아닙니다... <class 'complex'> (4+0j)
```

### 자료구조 변환

```py
name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
print(set(reversed(name)))
```

### 나의 문제풀이

```py
# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if '가을' in q1.keys():
    print('q1:', q1['가을'])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if '사과' in q2.values():
    print('q2:', '사과' in q2.values())

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
q3 = 90

if (q3 > 80):
    print('q3:', 'A 학점')
elif (q3 > 60):
    print('q3:', 'B 학점')
elif (q3 > 40):
    print('q3:', 'C 학점')
elif (q3 > 20):
    print('q3:', 'D 학점')
else:
    print('q3:', 'E 학점')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18
max = 0

if (a > b):
    max = a
elif (a < b):
    max = b

if(c > max):
    max = c
    print('q4:', 'max', max)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

q5 = '9703281'

if len(q5) != 7:
    print('잘못 입력한 주민번호입니다 다시 입력해주세요')

if(q5[6] == '1'):
    print('남자입니다')
elif(q5[6] == '3'):
    print('남자입니다')
elif(q5[6] == '2'):
    print('여자입니다')
elif(q5[6] == '4'):
    print('여자입니다')
else:
    print('잘못된 주민번호입니다')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q6 = ["갑", "을", "병", "정"]
list = []
for v in q6:
    if(v == '정'):
        continue
    list.append(v)

print('q6:', list)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

q7 = []

for v in range(1, 101, 2):
    q7.append(v)

print('q7:', q7)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q8 = ["nice", "study", "python", "anaconda", "!"]
list = []
for v in q8:
    if(len(v) >= 5):
        list.append(v)

print('q8:', list)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q9 = ["A", "b", "c", "D", "e", "F", "G", "h"]
list = []
for v in q9:
    if v.islower():
        list.append(v)

print('q9:', list)


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q10 = ["A", "b", "c", "D", "e", "F", "G", "h"]
list = []

for v in q10:
    if v.isupper():
        list.append(v)
print('q10:', list)

```

<details>
<summary>선생님 풀이 보기</summary>

```py
# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
import math
q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# case 1

for k in q1.keys():
    if k == '가을':
        print(q1[k])
# case 2

for k, v in q1.items():
    if k == '가을':
        print(v)

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.

q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q2.items():
    if v == '사과':
        print(k, v)
        break
else:
    print('사과 없음')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 100
grade = ''
if 0 < score > 100:
    grade = '나가'
elif score > 80:
    grade = 'A'
elif score > 60:
    grade = 'B'
elif score > 40:
    grade = 'C'
elif score > 20:
    grade = 'D'
elif score >= 0:
    grade = 'E'

print(grade)


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18
best = 0

best = a
if b > a:
    best = b
if c > b:
    best = c

print('max:', max(a, b, c))

print(best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

s = '891022-2473837'
if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

print(''.join([s for s in q3 if s != '정']))

q3_2 = [x for x in q3 if x != '정']
print('q3_2:', q3_2)

# 7. 1부터 100까지 자연수 중 '홀수'만 🔥 한 라인 🔥 으로 출력 하세요.

# case1

print(' '.join([str(s) for s in range(1, 100) if int(s) % 2 == 1]))

# case 2

for n in range(1, 101):
    if n % 2 != 0:
        print(n, end=',')  # 🔥 end 사용

print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

# case 1

print([s for s in q4 if len(s) >= 5])

print()

# case 2

for v in q4:
    if len(v) >= 5:
        print(v, end='')

print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

# case 1

print([s for s in q5 if s.islower()])

print()

# case 2

for v in q5:
    if v.isupper():
        continue
    else:
        print(v, end='')

print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

# case 1

print([s.upper() if s.islower() else s.lower() for s in q5])

# case 2

for v in q6:
    if v.isupper():
        print(v.lower())
    else:
        print(v.upper())

```

</details>

### 느낀점

`q4, q5`가 js의 lint와 달라져서 값이 다르게 나온다

아직 파이썬의 기본 문법을 제대로 숙달하지 않은 느낌이다

`q5`는 input을 받을 때 숫자를 입력하더라도 e.target.value의 값이 문자열로 넘어오게 된다

이를 바로 넘겨받은 string 값을 바로 정수형 int로 형변환하고 싶었는데 의도대로 잘 되지 않았다 강의를 보고 해당 부분만 어떻게 처리하는지 봐야할 것 같다

`end = ''` 문법을 잘 사용하지 않았던 것 같다.

문자열을 한 줄로 나열할 때 굳이 리스트로 만들지 않더라도 end 옵션을 통해 한줄로 나열할 수 있음을 명심하자

## 2021.10.17, day 06

### 리스트 컴프리헨션

```py
# 리스트를 쉽게 만들게 해주는 것

# 기존

numbers = []

for n in range(1, 101):
    numbers.append(n)

print(numbers)

print()

```

### 선언하기

```py
# 선언하는 법

# x = [x for x in range(범위)]
# x = [x for x in range(범위) if 조건문] >> 조건문이 true일 때 x로 append가 된다
# x = [x for x in range(범위) if 조건문 else 조건문] >>> 조건문이 false 일 때 적용할 것 적을 수 있다
```

```py
# 리스트 컴프리핸션

numbers2 = [x for x in range(1, 101)]
print(numbers2)

```

### 함수 정의 및 람다(lambda) 사용

- 함수 선언
- 함수 다양한 사용
- 다양한 반환 값
- \*args, \*\*kwargs
- 람다함수

### 함수 선언

```py
# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출

# 함수명()
# 함수명(parameter)

# 함수 선언 위치 중요
```

### 함수 다양한 사용

```py
# 예제 1 반환문 없이 사용

def hello(world):
    print('Hello', world)


hello('준희!')
hello('Python!')
hello(7777)
```

```py
# 예제 2 (리턴 사용)


def hello_return(world):
    val = 'Hello' + str(world)
    return val


str = hello_return('Junhee')

print(str)
```

```py
# 예제 3 (다중 리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)
```

### 다양한 반환 값

```py
# 예제 4 (데이터 타입 반환)
# 리스트 타입


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul2(100)
print(lt)

# 튜플 타입


def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)


tp = func_mul3(100)
print(tp)
```

### \*args, \*\*kwargs

```py
# 예제 5
# *args (arguments), *kwargs (keyword arguments)

# *args >> 가변 (JS의 REST Parameter와 동일)
# 튜플의 형태로 넘어온다


def args_func(*args):
    # print(type(args))
    print(args)

# 따라서 반복문을 사용할 수도 있다


def args_func2(*args):
    for t in args:
        print(t)

# enumerable >>> 인덱스를 통해 인덱스와 요소를 열거


def args_func3(*args):
    # for i, v in enumerate(range(10)) 범위 설정도 가능
    for i, v in enumerate(args):
        print(i, v)


args_func('kim')
args_func('kim', 'lee')
args_func('kim', 'lee', 'park')

args_func2('kim', 'lee', 'park')

args_func3('kim', 'lee', 'park')

print()

# kwargs


def kwargs_func(**kwargs):
    print(kwargs)


def kwargs_func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1='Kim', name2='Park', name3='Lee')
kwargs_func2(name1='Kim', name2='Park', name3='Lee')

print()

# 전체 혼합


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(1, 2)  # 1 2 () {}
example_mul(1, 2, 3)  # 1 2 (3) {}
example_mul(1, 2, 3, 4, name1='kim', name2='lee')  # 1 2 (3, 4) {'name': 'kim'}

print()
```

### 중첩함수 (클로저)

```py
# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print('in func')
    func_in_func(num + 1000)


nested_func(1000)
```

### 힌트

```py
# 예제 6 힌트 (타입 설정 but, 타입이 다르더라도 에러를 발생시키지는 않는다)

def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(5))
print(func_mul3(6.0))
```

### 람다함수

```py
# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적인 함수 -> 변수 할당


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)  # <function mul_10 at 0x10abb6830> 함수 선언시에 메모리에 이미 할당되어 있다
print(type(var_func))  # <class 'function'>

print(var_func(10))

# 람다식
# 불필요한 리턴문을 다 없앰, 메모리에 할당되지 않음

# lambda_mul_10= lambda num: num * 10


def lambda_mul_10(num): return num * 10


print('>>>', lambda_mul_10(10))


def func_final(x, y, func):
    print(x*y*func(10))


func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x*1000))
```

### 클래스 선언 및 Self 의 이해

- 클래스 선언
- 클래스 네임스페이스 Self
- 클래스, 인스턴스 변수
- Self

### 클래스 선언

```py
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

# 각 인스턴스의 id를 볼 수 있음

print('id:', id(user1))
print('id:', id(user2))

print()

# 각 인스턴스의 딕셔너리형 구조를 볼 수 있음 { key: value } 형식

print(user1.__dict__)
print(user2.__dict__)
```

## 2021.10.19, day 07

### 클래스, 인스턴스, 네임스페이스

```py
# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이
# 클래스 형태로 코딩을 한뒤 변수화하여
# 인스턴스에 할당하고 메모리에 올려 이를 사용한다

# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간, 모든 자료형은 자신만의 네임스페이스를 가진다
# 클래스 변수 : 직접 사용 가능 (js의 정적 메서드와 동일), 객체 보다 먼저 생성 , 해당 클래스를 사용하는 전체가 공유
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후에 사용, 각각이 개인적으로 가짐
```

```py
# 선언

# class 클래스명:
#     함수
#     함수1
#     함수2

# 예제 1

# 첫글자가 대문자로 시작하는 것을 원칙으로 함
# 단어와 단어 사이에는 대문자로 구분

# 초기화
class UserInfo:
    # ① 속성(프로퍼티), ② 메서드로 구분된다
    # 1. __init__ 을 통해 초기화를 헤야 한다
    #
    def __init__(self, name):
        self.name = name
        print('초기화!')

    def user_info_p(self):
        print("Name:", self.name)
```

### self의 이해

일반적으로 js에서의 this와 같은 의미로 쓰인다고 생각하면 될 것 같다

```py
# 예제 2
# self의 이해


class Parent:
    # self 인자가 없을 경우, 인스턴스 생성 시에 사용할 수 없다
    def function1():
        print('non self function called!')

    def function2(self):
        print(id(self))
        print('self function called!')


child = Parent()

# Parent.function1()
# >>> 인스턴스로 만들었을 경우 finction1() 메서드는 self 키워드가 없어 누구의 인스턴스인지 알 수 없다
# 따라서 self 가 없는 (자바스크립트에서의 정적 메서드) 클래스 메서드를 사용할 때는 클래스를 직접 호출하여 사용한다

Parent.function1()

child.function2()

print(id(child))

Parent.function2(child)
```

### 클래스 변수, 인스턴스 변수

- 클래스 변수는 self가 없다 (js의 정적 메서드와 동일)
- 인스턴스 변수는 self가 있다 (js의 this와 동일)

```py
# 예제 3
# 클래스 변수 (self x), 인스턴스 변수 (self o)


class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        # 클래스 변수는 self가 없기 때문에 클래스 명을 통해 직접 접근해야 한다
        WareHouse.stock_num += 1

    def __del__(self):
        # 클래스 변수는 self가 없기 때문에 클래스 명을 통해 직접 접근해야 한다
        WareHouse.stock_num -= 1


user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print()

print(WareHouse.__dict__)
# ... 'stock_num': 3, 클래스 변수는 사용자 모두가 공유하기 때문에, init(초기화)한 멤버 수만큼 증가하여 3이 되었다

print()

print(user1.name)
print(user2.name)
print(user3.name)

print()

# 자기 네임 스페이스에 없다면 클래스 네임스페이스에서 찾는다
# 클래스 네임스페이스에도 없다면 에러를 발생시킨다

print(user1.stock_num)  # 3
print(user2.stock_num)  # 3
print(user3.stock_num)  # 3

print()

# user1을 지울 경우
# 공통 클래스 변수인 stock에 할당된 값도 줄어들 것이다

del user1

print(user2.stock_num)  # 2
print(user3.stock_num)  # 2

```

### 클래스 상속, 다중 상속

- 클래스 상속
- 클래스 상속 예제 코디
- 클래스 다중 상속

### 클래스 상속

```py
# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 상속받을 경우 부모의 모든 속성, 메서드 사용 가능

# 라면 클래스를 만든다고 가정
# 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
  # 문자열로 무슨 클래스인지 적어주면 좋다
    """Parent Class"""

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        # super() 부모에게 상속받은 type, color라는 의미
        # 인스턴스 > BmwCar 클래스 > Car 클래스로 전달되는 상황이다
        # car_name을 제외한 type과 color는 재사용을 위해서 Car 클래스로부터 상속받고 있는 상황이므로
        # 인스턴스 생성 시에 넘겨받은 인수를 super(), 부모에게 넘겨준다
        super().__init__(type, color)  # super() 부모에게 상속받은 type, color라는 의미
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name :%s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        # super() 부모에게 상속받은 type, color라는 의미
        # 인스턴스 > Benz 클래스 > Car 클래스로 전달되는 상황이다
        # car_name을 제외한 type과 color는 재사용을 위해서 Car 클래스로부터 상속받고 있는 상황이므로
        # 인스턴스 생성 시에 넘겨받은 인수를 super(), 부모에게 넘겨준다
        super().__init__(type, color)  # super() 부모에게 상속받은 type, color라는 의미
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name :%s" % self.car_name

    # 자식 클래스에서도 부모와 같은 메서드를 선언할 경우
    def show(self):
        # 부모의 메서드도 다이렉트로 호출하고 싶을 경우에는 부모의 show 메서드를 super를 통해 선언해준다
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


model1 = BmwCar('520d', 'sedan', 'blue')

# 프로퍼티

print(model1.color)  # Super 부모로부터 옴
print(model1.type)  # Super 부모로부터 옴
print(model1.car_name)  # Sub 자식으로부터 옴

print()

# 메서드

print(model1.show())  # Super
print(model1.show_model())  # Sub

print()

print(model1.__dict__)
# >>> {'type': 'sedan', 'color': 'blue', 'car_name': '520d'}

# Method Overriding(오버라이딩) 올라타다

# 자식 클래스를 통해 인스턴스를 만들었을 때
# 부모에 있는 메서드(show)를 자식에서 동일한 이름(show)으로 선언할 경우 자식에 선언된 메서드로 '오버라이딩' 된다

model2 = BenzCar('220d', 'suv', 'black')

print(model1.show())  # Car Class "Show Method!"
print(model2.show())

# 부모 클래스의 show 메서드도 동시에 출력 >>> print(super().show())
# Car Class "Show Method!"
# Car Info : 220d suv black

print()

# Parent Method Call

model3 = BenzCar('400d', 'suv', 'navy')
print(model3.show())

print()

# Inheritance info (상속 정보를 리스트 형태로 반환한다)
# mro() 메서드를 통해 상속의 정보를 확인할 수 있다

print(BmwCar.mro())

# >>> [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]

print(BenzCar.mro())

# >>> [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]

print()
```

### 클래스 다중 상속

```py
# 예제 2
# 다중 상속


class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())

# [
# <class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>,
# <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>
# ]

# 다중 상속이 가능하나 너무나 복잡한 다중 상속은 코드를 구현하는데 어려움이 있을 수 있다

print()

print(A.mro())

# [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]

```

## 2021.10.20, day 08

### 모듈, 패키지

- 패키지 설정
- 모듈 사용 및 Alias(= as) 설정
- 패키지 사용 장점

```py
# 파이썬 모듈과 패키지

# 모듈 - 미리 구성해놓은 함수, 프로퍼티들을 재사용하기 위해 모아놓는 파일 단위
# 패키지 - 모듈들의 모음

# 패키지 예제

# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1, 클래스 형태 내부에 함수가 있을 때
# 클래스를 불러와야 하는 경우 (ex: import Fibonacci)
# from 문을 통해 해당 클래스의 위치를 기입해줘야 한다! 🔥

# from math_pkg.fibonacci import Fibonacci

import builtins
import math_pkg.prints as p
import math_pkg.calculations as c

from math_pkg.fibonacci import Fibonacci
from math_pkg.fibonacci import Fibonacci as fb
from math_pkg.calculations import div as d

print("ex1 :", end='')
Fibonacci.fibo(300)

print()

print("ex2 :", Fibonacci.fibo2(400))
print("ex2 :", Fibonacci().title)

# 사용2, (클래스), * 로 모듈의 기능 전체를 가져오기, 권장 x, 메모리를 많이 먹는다

# from math_pkg.fibonaccit import *

print()

# 사용3, (클래스) alias 주기 (as = alias)
# 가독성을 위해 as 를 통해 import 하는 클래스의 이름을 줄임말로 사용할 수 있다

# from math_pkg.fibonaccit import Fibonacci as fb (린팅에 의해 위로 올라가기 때문에 주석처리)

print("ex3 :", fb.fibo2(400))
print("ex3 :", fb().title)

print()

# 사용4, (함수)
# 모듈 전체 불러오기 + alias 사용하기

# import math_pkg.calculations as c

print("ex4 :", c.add(10, 20))
print("ex4 :", c.mul(10, 20))
print("ex4 :", c.div(10, 20))

print()

# 사용5, (함수)
# 일부만 불러오기

# from math_pkg.calculations import div as d

print("ex5 :", int(d(100, 10)))

print()

# 사용6

# import math_pkg.prints as p

p.print1()
p.print2()

# 빌트인 내장 모듈 보기
print(dir(builtins))

```

### 파일 Read, Write

- Open 함수
- 파일 모드의 이해
- 파일 읽기 실습
- 파일 쓰기 실습

```py
# 파일 읽기, 쓰기

# 읽기 모드 : r(read)
# 쓰기 모드(기존 파일 삭제 후 덮어 쓰기) : w(write)
# 추가 모드(파일 생성 또는 추가) : a(append)

# .. : 상대경로,
# . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제 1

from random import randint

f = open('./resource/review.txt', 'r')
content = f.read()
print(content)

print()
# f 변수에 할당된 인스턴스를 볼 수 있다
print(dir(f))

print()
# 반드시 close로 리소스를 반환해야 한다
f.close()

# 예제 2 (with 문 사용)
# with 문 사용 시, close()를 사용하지 않아도 요청이 종료된다

with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    # print(iter(c))

print()

# 예제 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print()
print()

# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>>> ', content)

    # 문서를 읽는 커서가 제일 밑으로 온 경우 더 이상 가져오지 않는다 (빈 내용을 가져온다)
    # 따라서 내용이 없다
    content = f.read()
    print('>>> ', content)

print()
print()

# 예제 5 (한 문장 단위로 읽어 올 때)
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' #### ')
        line = f.readline()

print()
print()

# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' ****** ')

print()
print()

# 예제 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('avg :{:6.3}'.format(sum(score)/len(score)))


print()
print()

# 파일 쓰기

# 예제 1 'w'
with open('./resource/test1.txt', 'w') as f:
    f.write('Nice man!\n')

# 예제 2 'a'
with open('./resource/test1.txt', 'a') as f:
    f.write('good man!\n')

# 예제 3

# from random import randint 랜덤 인트 만들기

with open('./resource/test2.txt', 'w') as f:
    for cnt in range(7):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제 4

# readlines : 리스트형태로 파일을 읽어오는 형태
# writelines : 리스트 -> 파일로 저장하는 형태
with open('./resource/test3.txt', 'w') as f:
    list = ['kim\n', 'park\n', 'lee\n']
    f.writelines(list)

# 예제 5

# 프린트 문으로 파일에 직접 문자열 적어주기
with open('./resource/test4.txt', 'w') as f:
    print('test Contents1!', file=f)
    print('test Contents2!', file=f)

```

### 다양한 Exceptions

- 파이썬 예외 종류
- 문법적 에러 발생 실습
- 런타임 에러 발생 실습
- Try-except-else-finally

```py
# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요하다
# linter : 코드 스타일, 문법 체크

# ① SyntaxError (문법 에러) : 잘못된 문법

print('Test)
# SyntaxError: unterminated string literal (detected at line 10)

# if True >>> SyntaxError: expected ':'
#  pass
# x => y

# ② NameError : 참조 변수가 없을 때 생기는 에러

import time

a = 10
b = 15

print(c)
# NameError: name 'c' is not defined

# ③ ZeroDivisionError : 0 나누기 에러

print(10 / 0)
# ZeroDivisionError: division by zero

# ④ IndexError : 인덱스 범위가 오버(넘쳤을)됐을 때

x = [10, 20, 30]
print(x[0])
print(x[3]) # >>> IndexError: list index out of range

# ⑤ KeyError (Dictionaries에 Key가 없을 때)

dic = {'name': 'Kim', 'Age': 33, 'city': 'Seoul'}
print(dic['hobby']) # >>> KeyError: 'hobby'

print(dic.get('hobby'))  # >>> None

# ⑥ AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

# import time

print(time.time())
print(time.month()) # >>> AttributeError: module 'time' has no attribute 'month'

# ⑦ valueError : 참조 값이 없을 때 발생

x = [1, 5, 9]

x.remove(10)  # >>> ValueError: list.remove(x): x not in list
# x.index(10)

# ⓼ FileNotFoundError 경로를 찾을 수 없을 때

f = open('test.txt', 'r') # >>> FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# ⑨ TypeError

x = [1, 2]
y = (3, 4, 5)
z = 'test'

print(x + y) # >>> TypeError: can only concatenate list (not "tuple") to list
# print(x + z)

# 따라서 형 변환이 필요하다
print(x + list(y))

# 항상 예외가 발새앟지 않을 것으로 가정하고 먼저 코딩을 해야 한다!
# 그 후 런타임 예외 발생시 예외 처리 코딩하는 단계를 권장한다(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1

# name = ['kim', 'lee', 'park']

# try:
#     z = 'kim'
#     # z = 'shin'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except ValueError:
#     print('Not Found it! - Occured valueError! ')
# else:
#     print('Ok! else!')

print()

# 예제 2

name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    # z = 'shin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:  # Error 의 종류를 적지 않으면 모든 Error가 해당 except로 들어온다
    print('Not Found it! - Occured valueError! ')
else:
    print('Ok! else!')

```

## 2021.10.21, day 09

### 다양한 Exceptions 이어서

```py
# name = ['kim', 'lee', 'park']

# try:
#     z = 'kim'
#     # z = 'shin'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except:  # Error 의 종류를 적지 않으면 모든 Error가 해당 except로 들어온다
#     print('Not Found it! - Occured valueError! ')
# else:
#     print('Ok! else!')

# 예제3

# name = ['kim', 'lee', 'park']

# try:
#     z = 'kim'
#     # z = 'shin'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except:  # Error 의 종류를 적지 않으면 모든 Error가 해당 except로 들어온다
#     print('Not Found it! - Occured valueError! ')
# else:
#     print('Ok! else!')
# finally:
#     print('무조건 실행!')

# 예제 4
# 예외처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('OK Finally')

# 예제 5

# 에러를 계층적으로 잡기
# 가장 방대한 에러를 다루는 기본 except는 가장 마지막에 적어주는 것이 좋다

name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    # z = 'shin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as v:
    print('Not Found it! - Occured value Error! ')
    print(v)
except IndexError:
    print('Not Found it! - Occured index Error! ')
except Exception:
    print('Not Found it! - Occured Error! ')
else:
    print('Ok! else!')
finally:
    print('무조건 실행!')

print()

# 예제 6
# 예외를 직접 방생 : raise: 일으키다
# raise 키워드로 예외 직접 발생

try:
    # a = 'Lee'
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가')
    else:  # '김'이 아닌 경우네는 ValueError를 발생시키도록 프로그램을 구현해놓음
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:  # 다 통과될 경우
    print('done')

```

### Excel, CSV 처리

- CSV 읽기
- CSV 쓰기
- XSL, XLSX 읽기
- 패키지 설치

```py
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import pandas as pd
import csv  # csv 파일을 읽기 위해서는 파이썬에서 기본 제공하는 csv 패키지를 import 해야 한다

# 예제 1
# 인코딩 에러로 인한 인코드 인수 추가 https://zephyrus1111.tistory.com/39

with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    # next(reader) Header (1행) 를 스킵한다

    # 확인
    print(reader)
    print(type(reader))

    print(dir(reader))
    print()

    for v in reader:
        print(v)

# 예제 2

with open('./resource/sample2.csv', 'r', encoding='euc-kr') as f:
    # reader = csv.reader(f) 없을 때 어떻게 보여지나 확인
    # delimiter=''를 통해 어떤 구분자로 구분되고 있나 적어준다
    reader = csv.reader(f, delimiter='|')
    # next(reader) Header (1행) 를 스킵한다

    # 확인
    print(reader)
    print(type(reader))

    print(dir(reader))
    print()

    for v in reader:
        print(v)

print()

# 예제 3 (Dict변환)
# Dictionary 형태로 가져오기 {'key':'value'}

with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.DictReader(f)
    for ele in reader:
        for k, v in ele.items():
            print(k, v)
        print('-----------------')

# 예제 4 (CSV 파일 쓰기)
# 순회하며 쓰기, for 문

w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w', encoding='euc-kr', newline='') as f:
    # newline = '' enter가 두칸씩 들어가지 않도록 처리하겠다
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제 5
# 한번에 쓰기 : writerows()

with open('./resource/sample4.csv', 'w', encoding='euc-kr', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

print()

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등이 있음
# pandas 를 주로 사용(openpyxl, xlrd)
# pandas 레퍼런스 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

# 해당 폴더의 가상환경 source ./activate 에서 설치해야 한다!

# pip install xlrd
# pip install openpyxl
# pip install pandas

# import pandas as pd >>> pandas 사용하기

# option
# sheetname='시트명' 또는 숫자, header = 3, skiprow = 숫자

xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인 (상위 5개)
print(xlsx.head())
print()

# 꼬리 데이터 확인 (하위 5개)
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape)  # 행 , 열 >>> (20, 7)

# 엑셀 or CSV 파일로 다시 쓰기

xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
```

### 데이터베이스 및 테이블 생성

- SQLite 기본 사용법
- 테이블 생성
- 데이터 삽입
- 기본 SQL 사용 예제

```py
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now:', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime:', nowDatetime)

# sqlite3
print('sqlite3.version :', sqlite3.version)
print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit (반영) / Rollback (되돌리기)
# 가상환경이 설정된 내부 디렉토리에서 받아야 하므로
# pwd 를 통해 현재 파일의 경로를 찾은 후, resource 디렉토리 내부에 database.db 라는 경로를 설정하였다
# isolation_level=None 을 통해 연결이 종료되었을 때 connection을 끊을 수 있도록 설정하였다.

conn = sqlite3.connect(
    '/Users/leejunhee/FastCampus/python_basic/resource/database.db', isolation_level=None)

# Cursor

c = conn.cursor()

print('Cursor Type:', type(c))
# print('Cursor Type:', dir(c))

# 테이블 생성(Data Type: TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# ? (물음표)로 처리된 데이터는 뒤에 튜플 형식으로 추가해줘야 한다
# 튜플 맨 마지막에는 ' , '를 추가해야 오류가 발생하지 않는다
c.execute("INSERT INTO users VALUES(1, 'LEE', 'junh0328@naver.com', '010-9170-1796', 'https://github.com/junh0328', ?)", (nowDatetime,))

```

## 2021.10.22, day 10

### 데이터베이스 및 테이블 생성 이어서...

```py
# 정석적인 데이터 삽입구조
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
          (2, 'Park', 'Park@daum.net', '010-1111-1111', 'park.com', nowDatetime))

```

### 데이터 다수 삽입

```py

# Many 삽입 (많은 데이터를 한번에 삽입하기) (튜플, 리스트 형태로 삽입하기)

userList = (
    (3, 'Cho', 'cho@naver.com', '010-2222-2222', 'cho.com', nowDatetime),
    (4, 'kim', 'kim@naver.com', '010-2222-2222', 'kim.com', nowDatetime),
    (5, 'Paik', 'Paik@naver.com', '010-2222-2222', 'paik.com', nowDatetime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
    VALUES (?,?,?,?,?,?)", userList)
```

### 데이터 삭제 / 커밋 / 롤백

```py
# 테이블 데이터 삭제
# rowcount를 통해 몇개의 데이터가 들어가있는지 확인할 수 있다.

conn.execute("DELETE FROM users")
print('users db deleted:', conn.execute(
    "DELETE FROM users").rowcount)  # >>> users db deleted: 5

# 커밋 (DB에 추가) : isolation_level = None 일 경우 자동으로 반영한다
conn.commit()

# 롤백 : 커밋한 데이터 되돌리기(없애기)
conn.rollback()

# 접속 해제
conn.close()
```

### 다양한 테이블 조회

- SQLite 기본 사용법
- SELECT
- Where
- Tuple, Dictionary Mapping

```py
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect(
    '/Users/leejunhee/FastCampus/python_basic/resource/database.db')  # 본인 DB 경로

# (마우스) 커서 바인딩 (Cursor Binding)
c = conn.cursor()

# 데이터 조회 (전체)
c.execute("SELECT * from users")

# 커서 위치가 변경
# 1개 로우 선택

print('One row -> \n', c.fetchone())
# One row -> (1, 'LEE', 'junh0328@naver.com', '010-9170-1796', 'https://github.com/junh0328', '2021-10-22 11:48:15')

# 지정 로우 선택
print('Three => \n', c.fetchmany(size=3))  # >>> 배열 형태로 로우 printing

# [
# (2, 'Park', 'Park@daum.net', '010-1111-1111', 'park.com', '2021-10-22 11:48:15'),
# (3, 'Cho', 'cho@naver.com', '010-2222-2222', 'cho.com', '2021-10-22 11:48:15'),
# (4, 'kim', 'kim@naver.com', '010-2222-2222', 'kim.com', '2021-10-22 11:48:15')
# ]

# 전체 로우 선택
print('All -> \n', c.fetchall())
# 남은 데이터를 리스트 형태로 가져옴 but, 현재 db에 5개만 저장했으므로 마지막 하나를 가져오는 결과

# >>> [(5, 'Paik', 'Paik@naver.com', '010-2222-2222', 'paik.com', '2021-10-22 11:48:15')]

# 만약 커서가 마지막 로우를 가리키는데 다시 로우를 불러온다면?
print('All -> \n', c.fetchall())

# 빈 배열을 가져온다
# >>> All -> []


# DB 순회 1

# rows = c.fetchall()
for row in rows:
    print('SELECT 1 >>>', row)

# DB 순회 2
for row in c.fetchall():
    print('SELECT2 >>>', row)

# DB 순회 3
for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    print('SELECT3 >>>', row)

# 보통 순회 2번을 많이 쓴다

print()

# WHERE Retrieve1
# 튜플 형식으로 가져오기
param1 = (3,)
c.execute('SELECT * FROM users WHERE id = ?', param1)
print('param1', c.fetchone())

# 3번 데이터는 하나이기 때문에 3번에 대한 데이터는 더 없으므로 빈 배열을 출력하게 된다
print('param1', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve2
# 정수형으로 가져오기
param2 = 4
c.execute('SELECT * FROM users WHERE id = "%s"' % param2)  # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve3
# 딕셔너리로 가져오기
c.execute('SELECT * FROM users WHERE id =:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve5
# c.execute("SELECT * FROM users WHERE id IN(?,?)", (3, 5))
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3, 5))
print('param5', c.fetchall())  # 데이터 없음


print()

# WHERE Retrieve6 (딕셔너리 형태)

c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall())  # 데이터 없음

print()

# Dump 출력
# DB 에 저장한 명령어 (SELECT, DELETE, CREATE, ...) 를 백업해두는 것
# >>> 현 폴더에서 dump.sql로 생성

with conn:
    with open('/Users/leejunhee/FastCampus/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close() 함수가 with문으로 인해 작성하지 않더라도 자동으로 동작한다
```

### 테이블 수정, 삭제

- UPDATE
- DELETE
- db 사용 권장 이유

### UPDATE & DELETE

```py
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

# DB 사용을 위한 패키지 import
import sqlite3

# DB 생성(파일)

conn = sqlite3.connect(
    '/Users/leejunhee/FastCampus/python_basic/resource/database.db')

# 해당 경로애 있는 db 파일 DB Brwoser for SQLite로 열기

# Cursor 연결
c = conn.cursor()

# 데이터 수정 1 (기본적인 형태로 수정하기 SQL 문법)
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

# 데이터 수정 2 (딕셔너리 형태로 수정하기)
c.execute("UPDATE users SET username = :name WHERE id = :id",
          {"name": 'goodman', "id": 3})

# # 데이터 수정 3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 4))

# 중간 데이터 확인 1

for user in c.execute("SELECT * FROM users"):
    print('user1:', user)


# 데이터 삭제 1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# 데이터 삭제 2 (딕셔너리 형태로 삭제하기)
c.execute("DELETE FROM users WHERE id = :id", {"id": 3})

# 데이터 삭제 3
c.execute("DELETE FROM users WHERE id = '%s'" % (4))
# c.execute("DELETE FROM users WHERE id = '%s'" % 4) >>> 튜플이 하나일 경우에는 소괄호를 적지 않아도 된다

print()

# 중간 데이터 확인 2

for user in c.execute("SELECT * FROM users"):
    print('user2:', user)

# 테이블 전체 데이터 삭제
print("user db deleted :", conn.execute("DELETE FROM users").rowcount, " rows")

# 커밋 : DB(SQLite)에 반영하기
conn.commit()

# 접속 해제
conn.close()

```

### db 권장 이유

- db는 여러사람이 관리해도 통합적으로 관리를 해준다
- 최신 데이터를 유지해준다
- 데이터의 무결성을 유지시켜준다

## 2021.10.23, day 11

# 타이핑 게임 기본 완성

- 단어 리스트 로드
- 총 게임 시간 측정
- 정답 개수 체크

```py
# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random   # 랜덤으로 불러오기 위함
import time     # 시간 측정을 위함

words = []      # 영어 단어 리스트(1000개 로드)

n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words)    # 단어 리스트 확인

input("Ready? Press Enter Key!")  # Enter Game Start!

start = time.time()  # 시작한 시간 (Start time)

while n <= 5:
    random.shuffle(words)  # words 단어를 섞는다
    q = random.choice(words)  # 뽑아와서 q 에 할당한다

    print()

    print("*Question # {}".format(n))
    print(q)      # 문제 출력

    x = input()   # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():
        print('Pass!')
        cor_cnt += 1
    else:
        print('Wrong!')

    n += 1

end = time.time()       # 끝난 시간 End Time
et = end - start        # 총 게임 시간
et = format(et, ".3f")  # 소숫점 세번째 자리까지 출력

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# 수행 시간 출력
print('게임 시간:', et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass
```

# 타이핑 게임 최종 완성

- 기록 결과 DB 저장
- 효과음 적용
- 최종 테스트

```py
# Section13-2
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random   # 랜덤으로 불러오기 위함
import time     # 시간 측정을 위함
import pygame   # 사운드 출력 필요 모듈
import sqlite3  # DB 입력을 위한 모듈
import datetime

# 소리 설정을 위한 모듈 사용

pygame.init()
pygame.mixer.init()
soundaGood = pygame.mixer.Sound('./sound/good.wav')
soundaBad = pygame.mixer.Sound('./sound/bad.wav')

# DB 생성 & Auto Commit
# 본인 DB 경로

# DB 파일 조회(없으면 새로 생성)
# 본인 DB 경로
# isolation_level=None 옵션을 주어야 auto commit 이 가능하다
conn = sqlite3.connect(
    '/Users/leejunhee/FastCampus/python_basic/resource/records.db', isolation_level=None)

# Cursor 연결

cursor = conn.cursor()

# 테이블 생성

cursor.execute(
    "CREATE TABLE IF NOT EXISTS records( id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")


words = []      # 영어 단어 리스트(1000개 로드)

n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words)    # 단어 리스트 확인

input("Ready? Press Enter Key!")  # Enter Game Start!

start = time.time()  # 시작한 시간 (Start time)

while n <= 5:
    random.shuffle(words)  # words 단어를 섞는다
    q = random.choice(words)  # 뽑아와서 q 에 할당한다

    print()

    print("*Question # {}".format(n))
    print(q)      # 문제 출력

    x = input()   # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():
        print('Pass!')
        cor_cnt += 1
        # 정답 소리 재생
        soundaGood.play()
    else:
        print('Wrong!')
        # 오답 소리 재생
        soundaBad.play()
    n += 1

end = time.time()       # 끝난 시간 End Time
et = end - start        # 총 게임 시간
et = format(et, ".3f")  # 소숫점 세번째 자리까지 출력

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# 기록 DB 삽입

cursor.execute("INSERT INTO records('cor_cnt','record','regdate') VALUES (?,?,?)",
               (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m=%d %H:%M:%S')))

# 수행 시간 출력
print('게임 시간:', et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass

```

# 파이썬 참조 심화

- 파이썬 객체 참조 다양한 특징
- Copy
- Deep Copy
- 매개변수 전달 주의할 점

```py
# Section14-1
# 파이썬 심화
# 객체 참조 중요한 특징들

# Python Object Reference

import copy  # Deep Copy를 위해 사용할 copy 모듈

print('EX1-1 -')
print(dir())  # directory, 현재 스코프에 위치한 환경을 보여줌

print()

# id vs __eq__ (== 같다 표시) 증명
# 객체 비교

x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y))
# >>> EX2-1 - 4335567680 4335567680

print('EX2-1 -', id(x.get('name')), id(y.get('name')))
# >>> EX2-1 - 4502354544 4502354544

# why?
# 객체의 경우 불변성의 특징을 가지는 원시 타입과 달리, 변하는 가변성의 성질을 가지고 있다.
# 만약 객체가 참조하는 메모리의 주소가 아닌 실제 값을 가지고 있다면, 객체 내부의 값이 변할 때마다 재할당해야 하므로 비용이 많이 든다

# 따라서 객체는 얕은 복사(shallow)를 통해 id 값에 메모리 주소를 참조하고 있다.
# 만약 같은 메모리 주소를 참조하고 있는 객체 내부의 데이터를 변경하면 어떻게 될까?

x['name'] = 'lee'

# 객체는 객체를 할당한 변수(x)가 기억하는 메모리 주소를 통해 메모리 공간에 접근하여 참조 값에 접근할 수 있다.
# 객체는 변경 불가능한 값이 아니므로, 재할당하지 않더라도 객체를 직접 변경할 수 있다.
# 객체를 삽입 수정 삭제 하더라도 메모리 주소가 변경되지 않는다는 것을 의미한다

print('EX2-2 -', 'x:', x, 'y:', y)
# >>> EX2-2 - x: {'name': 'lee', 'age': 33, 'city': 'Seoul'} y: {'name': 'lee', 'age': 33, 'city': 'Seoul'}
print('EX2-2 -', id(x), id(y))
# >>> EX2-2 - 4417651520 4417651520 , 앞서 EX2-1에서 확인했던 x,y의 id값 즉 메모리 주소가 변경되지 않았음을 알 수 있다

# 원시 타입에 대해 생각해보자
# 원시 타입의 경우 불변성(변하지 않는 성질)을 가진다
# 따라서 한번 선언된 기존 메모리에 존재하는 값을 변경할 수 없기 때문에, 재할당을 통해 새로운 주소에 값을 할당한다

str1 = 'lee'
str2 = str1

print('EX2-3 -', id(str1), id(str2))
# EX2-3 - 4320787440 4320787440

# str1에 'kim'이라는 문자열을 재할당한다면 str2도 'kim'을 참조할까?
# 객체와 같은 구조(가변성)라면 같은 주소를 가리키고 것이다
str1 = 'kim'

print('EX2-4 -', str1, str2)
print('EX2-4 -', id(str1), id(str2))
# EX2-4 - kim lee
# EX2-4 - 4376099440 4376345584

# 아니다, 문자열과 같은 원시 값의 경우 변경 불가능한 값이기 때문에 값을 직접 변경할 수 없다.
# 따라서 변수 값을 변경하기 위해 원시 값을 재할당(kim) 하면, 새로운 메모리 공간을 확보하고 재할당한 값을 저장한다
# 그렇기 때문에 참조하던 메모리 공간의 주소(id)가 변경된다 4320787440 > 4376345584

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__)는 값을 비교한다

print()
print()

# 튜플 불변형의 비교 (파이썬의 튜플은 불변성의 성질을 갖는다.)

tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
# >>> EX3-1 - 4361677760 4361677504
print('EX3-2 -', tuple1 is tuple2)  # 객체 주소(id) 비교
# >>> EX3-2 - False
print('EX3-3 -', tuple1 == tuple2)  # 값 비교
# >>> EX3-3 - True
print('EX3-4 -', tuple1.__eq__(tuple2))
# >>> EX3-4 - True

print()
print()

# Copy, Deepcopy(얕은 복사, 깊은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-2 -', tl1 is tl3)

# EX4-1 - True
# EX4-2 - True
# EX4-3 - True
# EX4-2 - False

print()

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)
print('external:', id(tl1[2]))

print()

tl1[1] += [110, 120]
tl1[2] += (110, 120)


print('EX4-8 -', tl1)
print('EX4-9 -', tl2)  # 튜플 재 할당(객체가 새로 생성됨, 메모리 주소가 변경됨)
print('EX4-10 -', tl3)
print('after:', id(tl1[2]))

print()
print()

# Deep Copy

# 장바구니


class Basket():
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)

# import copy


basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)      # 복사
basket3 = copy.deepcopy(basket1)  # 깊은 복사

print('EX5-1 -', id(basket1), id(basket2), id(basket3))
# >>> EX5-1 - 4318378352 4318377392 4318368128

print('EX5-2 -', id(basket1._products),
      id(basket2._products), id(basket3._products))
# >>> EX5-2 - 4345866816 4345866816 4345866688

# deep copy로 복사하지 않을 경우, 내부의 가리키는 데이터의 주소가 동일하다
# 그말인 즉, basket1의 Item을 변경하면, basket2의 Item이 변경될 수 있다는 의미이다
# 따라서 깊은 복사를 통해 객체가 동일한 메모리 주소를 참조하지 않도록 만들어줘야 한다

print()

# 증명
# 첫 번째 바구니는 오렌지를 넣고, 두 번째 바구니는 Snack을 빼고 싶은 경우

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)

print()
print()

# 함수 매개변수 전달 사용법


def mul(x, y):
    x += y
    return x


x = 10
y = 5


print('EX6-1 -', mul(10, 5), x, y)
# >>> EX6-1 - 15 10 5
print()

a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b)  # 가변형 a -> 원본 데이터 변경
# >>> EX6-2 - [10, 100, 5, 10] [10, 100, 5, 10] [5, 10]
# 원본 데이터 리스트 a 또한 변경된 상황

c = (10, 100)
d = (5, 10)

print('EX6-3 -', mul(c, d), c, d)  # 불변형 c -> 원본 데이터 변경 x
# >>> EX6-3 - (10, 100, 5, 10) (10, 100) (5, 10)

print()
print()

# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 x -> 참조 반환
# 어떻게 복사를 하던 하나의 id 값을 갖는다

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt1 is tt3, id(tt1), id(tt3))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'
ss3 = ss1


print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
print('EX7-5 -', ss1 is ss3, ss1 == ss3, id(ss1), id(ss3))

ss1 = 'Orange'

print('EX7-6 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
print('EX7-7 -', ss1 is ss3, ss1 == ss3, id(ss1), id(ss3))

```
