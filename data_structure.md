# 제로베이스 알고리즘 자료구조 51일 대비반 👨🏻‍💻

## 2021.10.25, day 12

### 자료구조란?

- 용어: 자료구조, 데이터 구조, data structure
- 대량의 데이터를 효율적으로 관리할 수 있는 데이터의 구조를 의미
- 코드 상에서 효율적으로 데이터를 처리하기 위해, 데이터 특성에 따라, 체계적으로 데이터를 구조화해야 함
- 어떤 데이터 구조를 사용하느냐에 따라, 코드 효율이 달라진다

#### 효율적으로 데이터를 관리하는 예

- 우편번호: 5자리 우편번호로 국가의 기초구역을 제공
- 5자리 우편번호에서 앞 3자리는 시, 군, 자치구를 표기, 뒤 2자리는 일련번호로 구성

- 학생 관리: 학년, 반, 번호를 학생에게 부여해서, 학생부를 관리
- XX학년, X반, X번 학생
- 만약 위 관리 기법이 없다면, 3000명 학생 중 특정 학생을 찾기 위해, 전체 학생부를 모두 훑어야 함

#### 대표적인 자료구조

- 배열, 스택, 큐, 링크드 리스트, 해쉬 테이블, 힙 등

> 현실 세계의 가장 대표적인 자료 구조 ? >>> 사전

### 알고리즘이란?

- 용어: 알고리즘, algorithm
- 어떤 문제를 풀기 위한 절차/방법
- 어떤 문제에 대해, 특정한 '엽력'을 넣으면, 원하는 '출력'을 얻을 수 있도록 만드는 프로그래밍
- ① 얼마나 효율적이냐(시간이 걸리느냐), ② 얼마의 저장 공간을 활용하느냐가 핵심 요소가 된다

> 현실 세계의 가장 대표적인 알고리즘? >>> 백종원 레시피

#### 자료구조와 알고리즘이 중요한 이유

- 어떤 자료구조와 알고리즘을 쓰느냐에 따라, 성능이 천지차이이다
- 결국 프로그래밍을 잘 할 수 있는 기술과 역량을 익히고, 검증할 수 있다

### 파이썬/ 주피터 노트북 설치

#### 프로그램 설치: anaconda 설치

- anaconda란?

  - 파이썬 기본(컴파일러)
  - 파이썬 주요 라이브러리
  - `jupyter notebook` 등 유용한 툴

- 참고

  - 컴파일러: 프로그래밍 언어로 작성된 코드를 컴퓨터가 실행할 수 있는 코드로 변환하는 프로그램ㅇ
  - 파이썬의 장점: 라이브러리

  `pip install 라이브러리 명`

#### jupyter notebook이란?

- Editor(PyCharm) VS jupyter notebook

  - 한줄 한줄 코드 실행 결과 확인이 쉽다
  - 문서와 코드를 함께 작성/저장할 수 있다

- 복잡한 자료구조/알고리즘을 보다 쉽게 정리하고, 익히기 위해 사용

## 2021.10.26, day 13

### `[자료구조]` 배열

#### 꼭 알아둬야 할 자료 구조: 배열 (Array)

- 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
- 파이썬에서는 리스트 타입이 배열 기능을 제공함

#### 1. 배열은 왜 필요할까?

- 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
- 같은 종류의 데이터를 순차적으로 저장
- 장점:

  - 빠른 접근 가능
  - 첫 데이터의 위치에서 상대적인 위치로 데이터 접근(인덱스 번호로 접근)

- 단점:

  - 데이터 추가/삭제의 어려움
  - 미리 최대 길이를 지정해야 함

#### make a list using C

- C 언어에서 배열을 사용할 경우 배열의 최대 길이를 사전에 정의해줘야 한다

```c
#include <stdio.h>

int main(int argc, char * argv[])
{
    char country[3] = "US";
    printf ("%c%c\n", country[0], country[1]);
    printf ("%s\n", country);
    return 0;
}
```

#### make a list using Python

- Python, JS의 경우 배열(문자열)의 길이를 사전에 정해주지 않아도 동작한다

```py
country = 'US'
print (country)

country = country + 'A'
print(country)
```

#### 2. 파이썬과 배열¶

- 파이썬에서는 리스트로 배열 구현 가능

```py
# 1차원 배열: 리스트로 구현시
data_list = [1, 2, 3, 4, 5]
data_list
```

```py
# 2차원 배열: 리스트로 구현시
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_list
```

```py
print (data_list[0])

print (data_list[0][0])
print (data_list[0][1])
print (data_list[0][2])
print (data_list[1][0])
print (data_list[1][1])
```

#### practice

- 위의 dataset 리스트에서 전체 이름 안에 'M'은 몇 번 나왔는지 빈도수 출력하기

```py
dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']
```

<details>
<summary>using python 🔥</summary>

```py
count = 0
for data in dataset:
    #     print('data:',data)
    for idx in range(len(data)):
        # print('data[idx]:', idx, data[idx])
        if data[idx] == 'M':
            count += 1

print('count:', count)

```

</details>

<details>
<summary>using JS 🔥</summary>

```js
for (x of dataset) {
  for (ele of x) {
    if (ele.indexOf("M") !== -1) cnt++;
  }
}

console.log(cnt);
```

</details>

#### 참고

- range(stop): range(10)은 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- range(start, stop): range(1, 11)은 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- range(start, stop, step): range(0, 20, 2)은 0, 2, 4, 6, 8, 10, 12, 14, 16, 18

  - start, stop, step은 음수로 지정 가능

### `[자료구조]` 큐 Queue

#### 1. 큐 구조

- 줄을 서는 행위와 유사
- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
- 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
- FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대

<img src="https://www.fun-coding.org/00_Images/queue.png" />

- 출처: http://www.stoimen.com/blog/2012/06/05/computer-algorithms-stack-and-queue-data-structure/

<img src="./images/queue.gif" alt="queue">

#### 2. 알아둘 용어

- Enqueue: 큐에 데이터를 넣는 기능 (JS에서 push)
- Dequeue: 큐에서 데이터를 꺼내는 기능 (JS에서 shift)

#### 3. 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기

- queue 라이브러리에는 다양한 큐 구조로 ① Queue(), ② LifoQueue(), ③ PriorityQueue() 제공
- 프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조를 사용

- Queue(): 가장 일반적인 큐 자료 구조
- LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
- PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

#### 3.x 큐 자료구조 모두 사용하기

<details>
<summary> Queue() </summary>

```py
# 큐 (Queue)

import queue

# FIFO QUEUE (일반적인 구조의 큐) 사용하기

data_queue = queue.Queue()

print('data_queue:', data_queue)
print('type:', type(data_queue))

print()

# 데이터 삽입 (put)

data_queue.put(1)
data_queue.put(2)
data_queue.put(3)

print('data_queue.qsize():', data_queue.qsize()) >>> 3

print()

# 데이터 추출 (get)

print('data_queue.get():', data_queue.get()) >>> 1
print('data_queue.get():', data_queue.get()) >>> 2
print('data_queue.get():', data_queue.get()) >>> 3

```

</details>

<details>
<summary> LifoQueue() </summary>

```py
import queue

# LIFO QUEUE (스택과 같은 구조의 큐) 사용하기

data_queue = queue.LifoQueue()

print('data_queue:', data_queue)
print('type:', type(data_queue))

print()

# 데이터 삽입 (put)

data_queue.put(1)
data_queue.put(2)
data_queue.put(3)

print('data_queue.qsize():', data_queue.qsize()) >>> 3

print()

# 데이터 추출 (get)

print('data_queue.get():', data_queue.get()) >>> 3
print('data_queue.get():', data_queue.get()) >>> 2
print('data_queue.get():', data_queue.get()) >>> 1

```

</details>

<details>
<summary> PriorityQueue() </summary>

```py
# PriorityQueue() 우선 순위가 있는 큐 만들기

import queue

data_queue = queue.PriorityQueue()

# - 튜플 형식 ( , )으로 데이터를 삽인한다
# - 숫자가 낮을수록 우선순위가 높다 (1 <<<<< 우선 순위가 높음 , .... , 15 <<<< 우선 순위가 낮음)
# - 우선순위가 높은 튜플이 먼저 Dequeue 된다

data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print()

print(data_queue.qsize())  # >>> 3

print()

print(data_queue.get())  # >>> (5,1)
print(data_queue.get())  # >>> (10, 'korea')
print(data_queue.get())  # >>> (15, 'china')
```

</details>

#### 참고) 어디에 큐가 많이 쓰일까?

- 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨 (운영체제 참조)

#### 4 프로그래밍 연습

**제공되는 queue 클래스 직접 구현해보기**

```py
queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)

print('queue_list:', queue_list)
# >>> queue_list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dequeue()

print('queue_list:', queue_list)
# >>> queue_list: [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

### `[자료구조]` 스택 Stack

#### 꼭 알아둬야 할 자료 구조: 스택 (Stack)

- 데이터를 제한적으로 접근할 수 있는 구조

  - 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조

- 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조

  - 큐: FIFO 정책
  - 스택: LIFO 정책

#### 1. 스택 구조

- 스택은 LIFO(Last In, Fisrt Out) 또는 FILO(First In, Last Out) 데이터 관리 방식을 따름

  - LIFO: 마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리 정책
  - FILO: 처음에 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책

- 대표적인 스택의 활용

  - 컴퓨터 내부의 프로세스 구조의 함수 동작 방식

- 주요 기능
  - push(): 데이터를 스택에 넣기
  - pop(): 데이터를 스택에서 꺼내기

<img src="./images/stack.gif" alt="stack">

### 2. 자료 구조 스택의 장단점

- 장점

  - 구조가 단순해서, 구현이 쉽다.
  - 데이터 저장/읽기 속도가 빠르다.

- 단점 (일반적인 스택 구현시)

  - 데이터 최대 갯수를 미리 정해야 한다. 🔥

    - 파이썬의 경우 재귀 함수는 1000번까지만 호출이 가능함

  - 저장 공간의 낭비가 발생할 수 있음

    - 미리 최대 갯수만큼 저장 공간을 확보해야 함

- 스택은 단순하고 빠른 성능을 위해 사용되므로, 보통 배열 구조를 활용해서 구현하는 것이 일반적임.
- 이 경우, 위에서 열거한 단점이 있을 수 있음

### 3. 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기

- append(push), pop 메서드 제공

```py
# 스택 (Stack)

# 큐와 달리 파이썬, JS 에서 기본 제공하는 리스트를 통해서 구현이 가능하다
# 큐의 경우 data = queue.Queue() 와 같이 인스턴스로 만들어서 사용했었음

# append: 삽입하기 (push)
# pop: 꺼내기 (pop)

data_stack = list()

data_stack.append(1)
data_stack.append(2)

print('data_stack:', data_stack) >>> [1,2]

print()

data_stack.pop()

print('① data_stack.pop():', data_stack) >>> [1]

print()

data_stack.pop()

print('② data_stack.pop():', data_stack) >>> [0]

```

### 4. 프로그래밍 연습

리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수를 사용하지 않고 직접 구현해보기)

```py
stack_list = list()


def push(data):
    stack_list.append(data)


def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data


for elem in range(10):
    push(elem)


print('stack_list', stack_list)
# >>> stack_list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print()

pop()

print('stack_list', stack_list)
# >>> stack_list [0, 1, 2, 3, 4, 5, 6, 7, 8]

```
