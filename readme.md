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

별개의 가상환경을 사용한다면 해당 가상 환경을 통해서 여러개의 다양한 버전의 파이썬과 모듈을 사용하더라도, 효과적으로 관리가 가능해진다

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
