## 빅-오 표기법과 시간 복잡도

- O(입력)

  - 입력 n에 따라 결정되는 시간 복잡도 함수
  - O(1), O( 𝑙𝑜𝑔𝑛 ), O(n), O(n 𝑙𝑜𝑔𝑛 ), O( 𝑛2 ), O( 2𝑛 ), O(n!)등으로 표기함
  - 입력 n의 크기에 따라 기하급수적으로 시간 복잡도가 늘어날 수 있음

  - O(1) < O( 𝑙𝑜𝑔𝑛 ) < O(n) < O(n 𝑙𝑜𝑔𝑛 ) < O( 𝑛2 ) < O( 2𝑛 ) < O(n!)

  | 빅오 표기법 | 명칭           |
  | :---------- | :------------- |
  | O(1)        | 상수 시간      |
  | O( 𝑙𝑜𝑔𝑛 )   | 로그 시간      |
  | O(n)        | 선형 시간      |
  | O(n 𝑙𝑜𝑔𝑛 )  | 로그 선형 시간 |
  | O( 𝑛2 )     | 이차 시간      |
  | O( 𝑛3 )     | 삼차 시간      |
  | O( 2𝑛 )     | 지수 시간      |

  |            | N이 1,000일 때의 연산 횟수 |
  | :--------- | :------------------------- |
  | O(n)       | 1,000                      |
  | O(n 𝑙𝑜𝑔𝑛 ) | 10,000                     |
  | O( 𝑛2 )    | 1,000,000                  |
  | O( 𝑛3 )    | 1,000,000,000              |

## 시간과 메모리 측정 하기

```py
import time

start_time = time.time() # 측정 시작

end_time = time.time() # 측정 종료
print('time :', end_time - start_time) # 수행 시간 출력
```

## 코딩 테스트를 위한 파이썬 문법

`지수`

```py
# 10억의 지수 표현 방식
a = 1e9
print(a)

# >>> 1000000000.0

# 752.5 만들기
a = 75.25e1
print(a)

# >>> 752.5

# 3.954 만들기
a = 3954e-3
print(a)

# >>> 3.954
```

## 리스트 컴프리헨션

```py
# case 1
array = [i for i in range(20) if i % 2 == 1]

print(array)

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

```py
# case 2
array = [i * i for i in range(1,10)]

print(array)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```py
# case 3 N X M 크기의 2차원 리스트를 초기화 하기

# N X M 크기의 2차원 리스트 초기화 (3 X 4 배열)

n = 3
m = 4

array = [[0] * m for _ in range(n)]

print(array)

[
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]
]
```

`언더바(_)는 어떤 역할인가요?`

반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바 `(_)`를 자주 사용합니다.

예를 들어 1부터 9까지의 자연수를 더할 때는 `case 1`처럼 작성하지만, 단순히 "Hello World"를 5번 출력할 때는 `case 2`처럼 언더바를 사용하여 무시할 수 있습니다.

```py
# case 1

summary = 0
for i in range(1,10):
  summary += i

print(summary)

45
```

```py
# case 2

for _ in range(5):
  print("Hello World")
```

## 리스트 관련 기타 메서드

| 메서드명  | 설명                                                                       | 시간 복잡도 |
| :-------- | :------------------------------------------------------------------------- | :---------- |
| append()  | 리스트에 원소를 하나 삽입할 때 사용                                        | O(1)        |
| sort()    | 기본 정렬 기능으로 오름차순으로 정렬 <br/>내림차순으로 정렬                | O(n 𝑙𝑜𝑔𝑛 )  |
| reverse() | 리스트의 원소의 순서를 모두 뒤집어 놓는다                                  | O(n)        |
| insert()  | 특정한 인덱스 위치에 원소를 삽입할 때 사용                                 | O(n)        |
| count()   | 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용                   | O(n)        |
| remove()  | 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거 | O(n)        |

```py
a = [1,4,3]
print("기본 리스트: ", a)

>>> [1, 4, 3]

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

>>> [1, 4, 3, 2]

# 오름차순으로 정렬
a.sort()
print("오름차순 정렬:", a)

>>> [1, 2, 3, 4]

# 내림차순으로 정렬
a.sort(reverse = True)
print("내림차순 정렬", a)

>>> [4, 3, 2, 1]

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

>>> [1, 2, 3, 4]

# 특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3 추가: ", a)

>>> [1, 2, 3, 3, 4]

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

>>> 2

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

>>> [2, 3, 3, 4]
```

코딩 테스트에서 `insert()`함수를 사용할 때 원소의 개수가 N개면, 시간 복잡도는 O(N)이다.

파이썬의 리스트 자료형의 `append()`함수는 O(1)에 수행되는 데에 반해 `insert(), remove()` 함수는 중간에 원소를

삽입 또는 삭제한 뒤에 원소 위치를 조정해줘야 하기 때문에 속도가 느릴 수 있다

```py
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

>>> [1, 2, 4]
```

## 집합(set) 자료형 관련 함수

```py
data = set([1, 2, 3])
print(data)
>>> {1, 2, 3}

# 새로운 원소 추가
data.add(4)
print(data)

>>> {1, 2, 3, 4}

# 새로운 원소 여러개 추가
data.update([5,6])
print(data)

>>> {1, 2, 3, 4, 5, 6}

# 특정 값을 갖는 원소 삭제
data.remove(3)
print(data)

>>> {1, 2, 4, 5, 6}
```

## 입출력

일반적으로 입력 과정에서는 먼저 데이터의 개수가 첫 번째 줄에 주어지고, 처리할 데이터는 그다음 줄에 주어지는 경우가 많다

```
입력 예시
5
65 90 75 34 99
```

```
출력 예시

99 90 75 65 34
```

### 입력을 위한 전형적인 소스 코드

```py
# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

>>>
5
65 90 75 34 99
[99, 90, 75, 65, 34]
```

### 공백을 기준으로 구분하여 적은 수의 데이터 입력

```py
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

>>>
3 5 7
3 5 7
```

## 주요 라이브러리

### sys 라이브러리

입력의 개수가 많은 경우에는 단순히 `input()`함수를 그대로 사용하지는 않는다.

이 경우 파이썬의 sys 라이브러리에 정의되어 있는 `sys.stdin.readline()` 함수를 이용한다.

```py
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

>>>
Hello World
Hello World
```

### itertools

itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.

가장 유용하게 사용할 수 있는 클래스는 `permutations (순열)`, `combination (조합)`이다.

`permutations`는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.

```py
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # 모든 순열 구하기

print(result)
>>>
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

`combinations`는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 (조합)를 계산한다.

```py
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)
>>>
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

`product`는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.

다만 원소를 중복하여 뽑는다.

```py
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)
>>>
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

`combinations_with_replacement`는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 (조합)를 계산한다.

다만 원소를 중복해서 뽑는다.

```py
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)
>>>
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```

### heapq

파이썬은 힙(heap) 자료구조 기능을 구현하기 위해 `heapq` 라이브러리를 제공한다.

`heapq`는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.

`heapq` 외에도 `PriorityQueue` 라이브러리를 사용할 수 있지만, 코딩 테스트 환경에서는 보통 `heapq`가 더 빠르게 동작한다.

파이썬의 힙은 최소 힙(min-heap)으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(n 𝑙𝑜𝑔𝑛 ) 오름차순 정렬이 완료된다.

힙에 원소를 삽입할 때는 `heapq.heappush()` 메서드를 사용하고

힙에서 원소를 꺼내고자 할 때는 `heapq.heappop()` 메서드를 이용한다.

```py
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result


result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

또한 파이썬에서는 최대 힙 (Max Heap)을 제공하지 않는다.

따라서 `heapq` 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.

최대 힙을 구현하여 내림차순 힙 정렬을 구현하는 예시는 다음과 같다.

> `-` 연산자의 위치를 주의해서 보자

```py
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(-heapq.heappop(h))
  return result


result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### bisect

파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 `bisect` 라이브러리를 제공한다.

`bisect` 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아낼 때 매우 효과적으로 사용된다.

bisect_left() 함수와 bisect_right() 함수가 가장 중요하게 사용되며, 이 두 함수는 시간 복잡도 O(n 𝑙𝑜𝑔𝑛 )에 동작한다.

```py
bisect_left(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a,x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
```

```py
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

2
4
```

### collections

파이썬의 `collections` 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리다.

`collections` 라이브러리의 기능 중에서 코딩 테스트에서 유용하게 사용되는 클래스는 `deque` 이다.

보통 파이썬에서는 `deque`를 사용해 큐를 구현한다.

일반 적인 리스트 자료형의 경우 append() 메서드로 데이터를 추가하거나, pop() 메서드로 데이터를 삭제할 때 '가장 뒤쪽의 원소'를 기준으로 수행한다.

따라서 앞쪽에 있는 원소를 처리할 때에는 리스트에 포함된 데이터의 개수에 따라서 많은 시간이 소요될 수 있다.

`deque` 클래스를 사용할 경우 이러한 복잡도를 효율적으로 관리할 수 있다.

|                            | 리스트 | deque |
| :------------------------- | :----- | :---- |
| 가장 앞쪽에 원소 추가      | O(N)   | O(1)  |
| 가장 뒤쪽에 원소 추가      | O(N)   | O(1)  |
| 가장 앞쪽에 있는 원소 제거 | O(N)   | O(1)  |
| 가장 뒤쪽에 있는 원소 제거 | O(N)   | O(1)  |

`deque`에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다. 다만, 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로 사용될 수 있다.

`deque`는 스택이나 큐의 기능을 모두 포함한다고 볼 수 있기 때문에 스택 혹은 큐 자료구조의 대용으로 사용될 수 있다.

```
popleft() : 가장 앞쪽에 있는 원소 제거
pop() : 가장 뒤에 있는 원소 제거

appendleft(x) : 가장 앞쪽에 원소 추가
append(x) : 가장 뒤쪽에 원소 추가
```

```py
# case 1 deque 사용
from collections import deque
import time

start_time = time.time()

data = deque([2,3,4])

data.appendleft(1)
data.append(5)

end_time = time.time()

print(data)
print(list(data))
print('end time:', end_time - start_time)

deque([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
end time: 0.0006029605865478516
```

```py
# case 2 리스트 사용

import time

start_time = time.time()

data = [2,3,4]

data.insert(0,1)
data.append(5)

end_time = time.time()

print(data)
print(list(data))
print('end time:', end_time - start_time)

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
end time: 9.059906005859375e-06
```

### math

math 라이브러리는 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리이다.

팩토리얼, 제곱근, 최대공약수 등을 계산해주는 기능을 포함하고 있으므로, 수학 계산을 요구하는 문제를 만났을 때 효과적으로 사용될 수 있다.

```py
import math

print(math.factorial(5))

print(math.sqrt(9))

print(math.gcd(21, 14))

120
3.0
7
```
