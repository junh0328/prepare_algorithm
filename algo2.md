# 제로베이스 알고리즘 자료구조 51일 대비반 👨🏻‍💻

## 그래프의 이해

### 1. 그래프 (Graph)란?

- 그래프는 실제 세계의 현상이나 사물을 정점(Vertex) 또는 노드(Node)와 간선(Edge)로 표현하기 위해 사용
- 예제 집에서 회사로 가는 경로를 그래프로 표현한 예

<img src="https://www.fun-coding.org/00_Images/graph.png" width=400>

### 2. 그래프 (Graph) 관련 용어

- 노드(Node) = 정점(Vertex): 위치를 말함
- 간선(Edge) = 링크 = 브랜치: 위치 간의 관계를 표시한 선으로 노드를 연결한 선이라고 보면 됨 (link 또는 branch라고도 함)
- 인접 정점(Adjacent Vertex): 간선으로 직접 연결된 정점(또는 노드)
- 참고 용어

  - 정점의 차수(Degree): 무방향 그래프에서 하나의 정점에 인접한 정점의 수
  - 진입 차수(In-Degree): 방향 그래프에서 외부에서 오는 간선의 수
  - 진출 차수(Out-Degree): 방향 그래프에서 외부로 향하는 간선의 수
  - 경로 길이(Path Length): 경로를 구성하기 위해 사용된 간선의 수
  - 사이클(Cycle): 단순 경로의 시작 정점과 종료 정점이 동일한 경우

<img src="https://www.fun-coding.org/00_Images/simplepath.png" width=200>

### 강사님의 픽

**눈여겨 볼 그래프 종류**

- 무방향 그래프
- 방향 그래프
- 가중치 그래프

### 3. 그래프 (Graph) 종류

### 무방향 그래프

- 방향이 없는 그래프
- 간선을 통해, 노드는 양방향으로 갈 수 있음
- 보통 노드 A,B가 연결되어 있을 경우 (A,B) 또는 (B,A)로 표기

<img src="https://www.fun-coding.org/00_Images/undirectedgraph.png" width=300>

### 방향 그래프 (Directed Graph)

- 간선에 방향이 있는 그래프
- 보통 노드 A, B가 A -> B 로 가는 간선으로 연결되어 있을 경우, `<A, B>` 로 표기 (`<B, A>` 는 `B -> A` 로 가는 간선이 있는 경우이므로 `<A, B>` 와 다름)

<img src="https://www.fun-coding.org/00_Images/directedgraph.png" width=300>

### 가중치 그래프 (Weighted Graph) 또는 네트워크 (Network)

- 간선에 비용 또는 가중치가 할당된 그래프

<img src="https://www.fun-coding.org/00_Images/weightedgraph.png" width=300>

### 연결 그래프 (Connected Graph) 와 비연결 그래프 (Disconnected Graph)

- 연결 그래프 (Connected Graph)

  - 무방향 그래프에 있는 모든 노드에 대해 항상 경로가 존재하는 경우

- 비연결 그래프 (Disconnected Graph)

  - 무방향 그래프에서 특정 노드에 대해 경로가 존재하지 않는 경우

### 비연결 그래프 예시 이미지

<img src="https://www.fun-coding.org/00_Images/disconnectedgraph.png" width=300>

### 사이클 (Cycle) 과 비순환 그래프 (Acyclic Graph)

- 사이클 (Cycle)

  - 단순 경로의 시작 노드와 종료 노드가 동일한 경우

- 비순환 그래프 (Acyclic Graph)

  - 사이클이 없는 그래프

### 비순환 그래프 예

<img src="https://www.fun-coding.org/00_Images/acyclicgraph.png" width=300>

### 완전 그래프 (Complete Graph)

- 그래프의 모든 노드가 서로 연결되어 있는 그래프

### 완전 그래프 예

<img src="https://www.fun-coding.org/00_Images/completegraph.png" width=300>

### 3. 그래프와 트리의 차이

### 트리는 그래프 중에 속한 특별한 종류라고 볼 수 있음 (트리는 그래프의 한 종류이다)

|                | 그래프                                             | 트리                                          |
| :------------: | :------------------------------------------------- | :-------------------------------------------- |
|      정의      | 노드와 노드를 연결하는 간선으로 표현되는 자료 구조 | 그래프의 한 종류, 방향성이 있는 비순환 그래프 |
|     방향성     | 방향 그래프, 무방향 그래프 둘 다 존재함            | 방향 그래프만 존재함                          |
|     사이클     | 사이클 가능함, 순환 및 비순환 그래프 모두 존재함   | 비순환 그래프로 사이클이 존재하지 않음        |
|   루트 노드    | 루트 노드 존재하지 않음                            | 루트 노드 존재함                              |
| 부모/자식 관계 | 부모 자식 개념이 존재하지 않음                     | 부모 자식 관계가 존재함                       |

## 너비 우선 탐색(BFS, Breadth-First Search)과 깊이 우선 탐색(DFS, Depth-First Search)

### 1. BFS와 DFS란?

- 대표적인 그래프 탐색 알고리즘
- 너비 우선 탐색 (BFS): 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식
- 깊이 우선 탐색 (DFS): 정점의 자식들을 먼저 탐색하는 방식

### BFS/DFS 방식 이해를 위한 예제

- BFS 방식: A - B - C - D - G - H - I - E - F - J

  - 한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 순회함

- DFS 방식: A - B - D - E - F - C - G - H - I - J

  - 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순화함

<img src="https://www.fun-coding.org/00_Images/BFSDFS.png" width=700>

### 2. 파이썬으로 그래프를 표현하는 방법

- 파이썬에서 제공하는 딕셔너리와 리스트 자료 구조를 활용해서 그래프를 표현할 수 있음

### BFS(너비 우선 탐색) 그래프 예와 파이썬의 표현

<img src="https://www.fun-coding.org/00_Images/bfsgraph.png" width=700>

```py
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)

>>>

{'A': ['B', 'C'],
 'B': ['A', 'D'],
 'C': ['A', 'G', 'H', 'I'],
 'D': ['B', 'E', 'F'],
 'E': ['D'],
 'F': ['D'],
 'G': ['C'],
 'H': ['C'],
 'I': ['C', 'J'],
 'J': ['I']}
```

### 3.1) BFS 알고리즘 구현

- 자료구조 큐(queue)를 활용한다
- need_visit (방문이 필요한 큐), visited(방문한 큐) 두 개의 큐를 생성

<img src="https://www.fun-coding.org/00_Images/bfsqueue.png" width=700>

### append / extend 차이점 알아보기

```py
# append vs extend 차이

#list.append(x)는 리스트 끝에 x 1개를 그대로 넣습니다.
#list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.


x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.append(y)
print('append x:', x)

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y)
print('extend x:', x)

print()

x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.append(y)
print('append x:', x)

x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.extend(y)
print('extend x:', x)

print()

x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.append(y)
print('append x:', x)

x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.extend(y)
print('extend x:', x)

>>>

append x: ['Tick', 'Tock', 'Song', ['Ping', 'Pong']]
extend x: ['Tick', 'Tock', 'Song', 'Ping', 'Pong']

append x: ['Tick', 'Tock', 'Song', [['Ping', 'Pong']]]
extend x: ['Tick', 'Tock', 'Song', ['Ping', 'Pong']]

append x: ['Tick', 'Tock', 'Song', 'Ping']
extend x: ['Tick', 'Tock', 'Song', 'P', 'i', 'n', 'g']
```

### BFS 구현하기

```py
def bfs(graph, start_node):
    # 방문했던 큐
    visited = list()
    # 방문이 필요한 큐
    need_visit = list()
    # 첫 스타팅 노드를 방문이 필요한 큐에 담는다
    need_visit.append(start_node)

    # 방문이 필요한 큐가 남아있는 동안 반복한다
    while need_visit:
        # need_visit 큐의 가장 앞에 있는 요소를 뽑아 node 변수에 할당한다
        node = need_visit.pop(0)
        # 방문했던 큐에 해당 노드가 존재하지 않는다면
        if node not in visited:
            # 방문했던 큐에 추가한다
            visited.append(node)
            # 주어진 그래프에 가장 앞에 있는 요소가 가지고 있던 요소들을 방문이 필요한 큐에 확장한다
            need_visit.extend(graph[node])

    return visited

>>> print(bfs(graph, 'A'))

['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
```

### BFS 시간 복잡도

- 일반적인 BFS 시간 복잡도

  - 노드 수 : V
  - 간선 수 : E

    - 위 코드에서 `while need_visit:` 는 V + E 번 만큼 수행함

  - 시간 복잡도 : O(V+E)

```py
# 시간 복잡도

def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print (count)
    return visited

bfs(graph, 'A')
>>>
19
```

### 3.2) DFS 알고리즘 구현

### DFS 그래프 예와 파이썬 표현

<img src="https://www.fun-coding.org/00_Images/dfsgraph.png" width=700>

- 자료구조 스택과 큐를 활용함
- need_visit 스택과 visited 큐, 두 개의 자료 구조를 생성
- **BFS에서는 둘 다 큐를 사용했었죠? 🔥**

```py
def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

dfs(graph, 'A')
>>>
['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
```

### DFS 시간 복잡도

BFS 시간 복잡도와 같음

```py
def dfs(graph, start_node):
    visited, need_visit = list(), list()

    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(count)
    return visited

dfs(graph, 'A')
>>>
19
['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
```

## 탐욕 알고리즘의 이해

### 1. 탐욕 알고리즘이란?

- 그리디 알고리즘 또는 탐욕 알고리즘 이라고 불림
- 최적의 해에 가까운 값을 구하기 위해 사용됨
- 여러 경우 중 하나를 결정해야할 때마다, 매순간 최적이라고 생각되는 경우를 선택하는 방식으로 진행해서, 최종적인 값을 구하는 방식

### 2. 탐욕 알고리즘 예

### 문제1: 동전 문제

- 지불해야 하는 값이 4720원일 때 1원, 50원, 100원, 500원 동전으로 동전의 수가 가장 적게 지불하는 경우를 구하시오
- 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
- 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨

```py
coin_list = [1, 100, 50, 500]

# cnt >> 동전의 수
# details >> 사용한 동전, 동전의 수

def solution(value, coin_list):
    cnt = 0
    details = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        # coin_num(10) = 5328 // 500
        coin_num = value // coin
        # cnt(10) += 10
        cnt += coin_num
        # value(320) -= 10 * 500
        value -= coin_num * coin
        # details >>> [500, 10]
        details.append([coin, coin_num])

    return cnt, details


print(solution(5320, coin_list))

>>>
(33, [[500, 10], [100, 3], [50, 0], [1, 20]])
```

### 문제2: 부분 배낭 문제 (Fractional Knapsack Problem)

- 무게 제한이 k인 배낭이 최대 가치를 가지도록 물건을 넣는 문제
- 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
- 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem 으로 부른다
- Fractional Knapsack Problem의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Knapsack Problem으로 부름)

| 물건(i) | 물건1 | 물건2 | 물건3 | 물건4 | 물건5 |
| :-----: | :---: | :---: | :---: | :---: | :---: |
| 무게(w) |  10   |  15   |  20   |  25   |  30   |
| 가치(v) |  10   |  12   |  10   |   8   |   5   |

해당 구조를 배열로 만든다면 다음과 같다

```py
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
```

```py
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def solution(data_list, max_weight):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        # 가방 하나가 온전히 들어 갔을 때
        if max_weight - data[0] >= 0:
            max_weight -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        # 가방 하나가 온전히 들어 가지 못했을 때
        else:
            # 비율로 계산하여 (무게를 나눠) 넣는다
            percentage = max_weight / data[0]
            total_value += data[1] * percentage
            details.append([data[0], data[1], percentage])
            break

    return total_value, details


print(solution(data_list, 29))

```
