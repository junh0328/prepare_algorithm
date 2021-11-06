# 제로베이스 알고리즘 자료구조 51일 대비반 👨🏻‍💻

## 대표적인 정렬 1: 버블 정렬 (bubble sort)

### 1. 정렬(sorting)이란?

- 정렬: 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
- 정렬은 프로그램 작성시 빈번하게 필요로 함
- 다양한 알고리즘이 고안되었으며, 알고리즘 학습의 필수
- 다양한 정렬 알고리즘 이해를 통해, 동일한 문제에 대한 다양한 알고리즘이 고안될 수 있음을 이해하고, 각 알고리즘 간 성능 비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음

### 2. 버블 정렬(bubble sort) 란?

- `두 인접한 데이터를 비교해서, ① 앞에 있는 데이터가 ② 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘`

<img src="./images/bubble_sort.gif.gif" alt="버블정렬">

출처 : https://visualgo.net/en/sorting

### 3. 어떻게 코드로 만들까?

`case 1: 데이터가 두 개일 때 버블 정렬 알고리즘 방식으로 정렬`

```py
arr = [5 , 2]

# 버블 정렬 탐색을 통해 맨 앞에서부터 2개의 인덱스를 비교하여 가장 큰 수가 뒤로 간다
if arr[1] < arr[0]:
    arr[1], arr[0] = arr[0], arr[1]

print(arr)
```

`case 2: 데이터가 세 개일 때 버블 정렬 알고리즘 방식으로 정렬`

```py
arr = [5,4,2]

if arr[1] < arr[0]:
    arr[1],arr[0] = arr[0], arr[1]
    if arr[2] < arr[1]:
        arr[2],arr[1] = arr[1], arr[2]
        if arr[1] < arr[0]:
            arr[1],arr[0] = arr[0], arr[1]
print(arr)
```

`case 3: 데이터가 네 개일 때 버블 정렬 알고리즘 방식으로 정렬`

- 다음과 같은 반복이 발견됨

| arr.length | 조건 체크 | 턴(순회) |
| :--------: | :-------: | :------: |
|     2      |     1     |    1     |
|     3      |     2     |    2     |
|     4      |     3     |    3     |

```py
arr = [5,2,3,1]

for index in range(배열의 길이 -1):
  for index 2 in range(배열의 길이 -1):
    if 앞 데이터 > 뒤 데이터:
      swap(앞 데이터, 뒤 데이터)
```

이를 바탕으로 arr의 길이가 n개일 때를 위한 코드 작성

```py
# 처음 작성한 코드

arr =[5,2,3,1,6,10, -1]

for index in range(len(arr)-1):
    for index2 in range(len(arr) -1):
        if arr[index2] > arr[index2 +1]:
            arr[index2], arr[index2+1] = arr[index2+1], arr[index2]

print('arr:', arr)
```

```py
# 이미 한 번 탐색마다 맨 뒤에는 최대 값이 고정되므로
# 2번째 순회를 돌 때는 배열의 맨 끝까지 탐색할 필요가 없다
# 따라서 for index2 in range(len(arr)- index -1): 와 같은 조건문이 나온다

arr =[5,2,3,1,6,10, -1]

for index in range(len(arr)-1):
    for index2 in range(len(arr)- index -1):
        if arr[index2] > arr[index2 +1]:
            arr[index2], arr[index2+1] = arr[index2+1], arr[index2]

print('arr:', arr)
```

**But, 데이터가 처음부터 정렬이 되어있을 경우 [1,2,3,4]에도 위의 반복문은 계속 순회를 해야 한다**

- 따라서 해당 데이터가 순회가 필요한지를 판단할 변수 swap (Boolean)를 추가하여 조건문에 넣어주었다

```py
def bubblesort(data):
    for index in range(len(data) - 1):
        # 초기에는 swap이 일어나지 않는다고 가정
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                # swap이 한 번 이라도 일어날 경우에는 True로 변경
                swap = True

        # 한번 순회를 했음에도 swap이 일어나지 않는다면, 반복을 중단하고 리턴한다
        if swap == False:
            break
    return data
```

### 5. 버블 정렬 알고리즘 분석

- 반복문이 두 개 O($n^2$)

  - 최악의 경우, <font size=5em>$\frac { n * (n - 1)}{ 2 }$</font>

- 완전 정렬이 되어 있는 상태라면 최선은 O(n)

## 대표적인 정렬 2: 선택 정렬 (selection sort)

### 1. 선택 정렬 (selection sort)란?

- 다음과 같은 순서를 반복하여 정렬하는 알고리즘
- 주어진 데이터 중 최소값을 찾음
- 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
- 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

<hr/>

- 1. 첫 번째 인덱스의 value를 특정 변수에 담음 >>> select
- 2. 배열을 순회하며 select에 저장된 value보다 작은 값이 있을 경우 select를 교체(재할당)
- 3. 해당 작업이 완료된 경우 다음 자리 (index +1) 부터 다시 순회 시작

<img src="./images/selection_sort.gif.gif" alt="선택 정렬">

| (stand)<br/>비교 데이터 인덱스 | (stand +1)<br/>비교 시작 인덱스 | (data.length)<br/>비교 끝 인덱스 |
| :----------------------------: | :-----------------------------: | :------------------------------: |
|               0                |                1                |                3                 |
|               1                |                2                |                3                 |
|               2                |                3                |                3                 |
|               n                |               n+1               |           data.length            |

```py
data = [5,4,3,1]

for stand in range(데이터의 길이 -1):
  lowest = stand
  for index in range(stand+1, 데이터의 길이):
    if data[lowest] > data[index]:
      lowest = index

  swap(lowest, stand)
```

```py
data = [5, 3, 1, 10, 9, -1]

# 1. 주어진 데이터 중, 최솟값을 찾음
# 2. 해당 최솟값을 데이터 맨 앞에 위치한 값과 교체함
# 3. 맨 앞의 위치(인덱스)를 뺀 다음 데이터부터 동일한 방법으로 1-2번 과정을 반복함


def selection_sort(data):
    for standard in range(len(data) - 1):
        lowest = standard
        for index in range(standard+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[standard], data[lowest] = data[lowest], data[standard]
    return data


print(selection_sort(data))
```

### 3. 선택 정렬 알고리즘 분석

- 반복문이 두 개 O($n^2$)

  - 실제로 상세하게 계산하면, <font size=5em>$\frac { n * (n - 1)}{ 2 }$</font>

## 대표적인 정렬 3: 삽입 정렬 (insertion sort)

### 1. 삽입 정렬 (insertion sort)란?

- 삽입 정렬은 `① 두 번째 인덱스`부터 시작
- `① 해당 값`을 차례대로 자신의 앞 인덱스가 가지는 value 값과 비교
- 앞 인덱스보다 `① 해당 값`이 더 작을 경우, 해당 인덱스 앞에 삽입 (swap)
- 앞 인덱스 앞에 또 다른 인덱스가 존재할 경우, 계속 앞으로 가며 value 값을 비교
- 자신의 값이 위치할 수 있는 자리(인덱스)에 삽입한다

<img src="./images/insert_sort.gif.gif" alt="삽입 정렬">

| 데이터 길이 | 조건 체크  | 턴  |
| :---------: | :--------: | :-: |
|      2      |     1      |  1  |
|      3      |  (최대) 2  |  2  |
|      4      |  (최대) 3  |  3  |
|      n      | (최대) n-1 | n-1 |

### 알아두면 좋은 range

```py
# range(a , b, -1)
# >>> a부터 b-1 까지 내림차순으로 반복한다

for index in range(10, 1, -1):
  print(index, end='')

>>> 10, 9, 8, 7, 6, 5, 4, 3, 2
```

### 알고리즘 구현

```py
for index in range(데이터의 길이 -1):
  for index2 in range(index+1, 0, -1):
    if data[index2] < data[index2-1]:
      data[index2], data[index2-1] = data[index2-1], data[index2]
    else:
      break
```

```py
data = [5, 2, 3, 1]


def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1, 0, -1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data


print(insertion_sort(data))

```

### 삽입 정렬 알고리즘 분석

- 반복문이 두 개 O($n^2$)

  - 최악의 경우, <font size=5em>$\frac { n * (n - 1)}{ 2 }$</font>

- 완전 정렬이 되어 있는 상태라면 최선은 O(n)
