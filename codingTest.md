# 대표 유형

코딩 테스트란

- 주어진 시간 동안
- 주어진 문제를
- 요구사항에 맞게
- 프로그래밍하여
- Accept나 점수를 받는 시험

## 과정

1. 문제
2. 모델링
3. 절차적 사고
4. 구현

## 종류

|               종류                |   유형   |
| :-------------------------------: | :------: |
|     파싱,해싱,정렬,시뮬레이션     |   구현   |
| 탐색(BFS/DFS), 완전탐색(백트래킹) |   탐색   |
|    자료구조(스택, 큐, 힙 등),.    |   구조   |
|       그리디, DP, 이분탐색        | 알고리즘 |

## 에러

|           종류           |     유형     |
| :----------------------: | :----------: |
|       컴파일 에러        |  문법 오류   |
|      시간 초과(TLE)      | 최적화 필요  |
|     메모리 초과(MLE)     | 최적화 필요  |
|     런타임 에러(RE)      |  과정 오류   |
| 틀렸습니다(Wrong Answer) | 수 많은 이유 |

## 틀렸습니다 ?

- 제한 및 대소 관계 (이상, 이하, 초과, 미만, min, max)
- 예외 처리 (단, 없는 경우는 -1을 출력한다)
- 입력과 출력 (공백, 양식, 순서, 정렬 유무)
- 시간 제한과 메모리 제한

## 내가 어려워하는 부분 찾기

### 문제 모델링이 어려워요

- 수치 및 조건 정리하기
- 전체적인 흐름 그리기
- 입출력 예제 이해하기

```py
# 10명의 ** 값이 정수로 주어진다면?

A = [int(input()) for i in range(10)]

# ~를 체크해야 한다
def check(x):
  pass
```

### 문제가 막혀요

- 필수 알고리즘은 암기 (다다익선)
- 설명과 함께 풀어보기/ 유형은 많이 풀기
- 모델링을 바탕으로 기능을 가볍게 적어보기

## 코딩 테스트 유형별 분석

### 구현

프로그래밍의 기초: 구현

구현:

- 어떤 내용이 구체적인 사실로 나타나게 함

- 문제 조건을 코드로 작성하여 돌아가게 함

내장 함수를 잘 사용하기

### 자료형의 기본 활용과 Tip

`기본 자료형`

| single(단일 자료) | container(다중 자료) |
| :---------------: | :------------------: |
|      Integer      |         List         |
|       Float       |        Tuple         |
|      String       |      Dictonary       |
|      Boolean      |         Set          |

### Integer

- 수의 크기 제한이 딱히 없음 > overFlow 걱정을 줄일 수 있음
- str()로 쉬운 형변환
- 연산/함수 사용 시, float로 변환되는 경우

  - 나눗셈은 `/`가 아닌 `//`로 안전하게 나눌 수 있음 (또는 divmod 사용)

```py
# 나누기
3 / 3 >>> 1.0

type(3/3) >>> float

## //로 나누기

3 // 3 >>> 1
type(3//3) >>> int

## divmod(a,b)
divmod(7,3)

>>> (2,1)
```

### String

- Immutable한 변수

  - List로 변환해서 사용하기

- `+` 연산과 `*` 연산 조심하기

  - join() method 활용하기

- .split() .replace() 등 다양한 method 활용이 초점
- Slicing을 자유롭게 할 수 있는 것
- Char를 ord와 chr로 다루기

```py
### ASCI 코드 변환

chr(65) >>> 'A'

ord('A') >>> 65
```

### Boolean

- 논리 연산과 활용
- Short Circuit

  - or 연산에 앞 항이 참
  - and 연산에 앞 항이 거짓

- 모든 문제의 기본: 참/거짓

```py
# Short Circuit의 활용


if 1//0:
    print('hello') >>> # ZeroDivisionError: integer division or modulo by zero

if 0 and 1//0:
    print('hello') >>> 'hello'

if 1 or 1//0:
    print('hello') >>> 'hello'

```

### List

- List Comprehension 사용하기
- sort와 sorted 구분하기
- len, sum, max, min 등 활용하기
- Slicing, `[-1]`emd dmatn dlseprtm ghkfdyd
- reduce, filter도 활용하면 좋음

```py
### List Comprehension

list_arr = [i for i in range(10)]
print(list_arr)

>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

### None List Comprehension

list_arr2 = list()

for i in range(10):
    list_arr2.append(i)

print(list_arr2)

>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```py
# sort & sorted

list = [3, 5, 6, 9, 2]

# sorted: 원본 배열을 변환시키지 않음
print(sorted(list))
>>> [2,3,5,6,9]

print(list)
>>> [3,5,6,9,2]

# sort: 원본 배열을 변환
list.sort()
print(list)

>>> [2,3,5,6,9]

```

### Tuple

- 초기 상태 표현시 코드가 길어지는 것 방지

  - ex) a,b,c = 0,0,0

- Map과 함께 사용하여 입력 받기

  - ex) a,b = map(int, input().split())

- 동시에 변해야하는 객체에 효율적 표현 가능

  - ex) a,b = b,a (swap)

```py
a, b = map(int, input().split())

print('a,b:', a, b)

>>>
3 7
a,b: 3 7
```

### Dictonary

- Keys나 values를 사용하여 효율적인 사용 추천
- 반복문 돌리기

  - ex) for a,b in dict_exam: ~

- 개인적으로는 문자열 자체를 index로 사용하고 싶은 경우

  - 단어나 알파벳 카운팅

### Set

- 중복 체크

  - set(list) 사용

- 합집합, 여집합, 차집합 등 집합 연산

  - 시간 복잡도가 크니 주의해서 사용

```py
st = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3])

print('st:', st)
>>> st: {1, 2, 3, 4, 5}
```

```py
# 중복 체크

def isCheck(list):
  return len(list) == len(set(list))
```

# 매개변수의 이해와 구조화

## Container의 역할

- 자료형에 따른 본인만의 container 설정과 이해

  - Tuple: 위치(index)에 따른 의미
  - Set: 포함 여부의 의미
  - List: index와 원소의 관계
  - Dict: key와 value의 관계

- 함수와 마찬가지로 적절한 명명 필요
