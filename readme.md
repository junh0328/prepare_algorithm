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
