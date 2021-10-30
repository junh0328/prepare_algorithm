# 노드 객체

# 노드 : 데이터 저장 단위 (데이터 값, 포인터로 구성)
# 포인터 : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


node1 = Node(1)

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

node = head  # node1이 Head다
while node.next:
    print(node.data)
    node = node.next
print('no more head', node.data)

print()

# -----------------------------------------------------------

# 링크드 리스트의 복잡한 기능 1 (링크드 리스트 데이터 사이에 데이터를 추가하기)

node3 = Node(1.5)

print(node3.data)  # >>> 1.5
print(node3.next)  # >>> None, why? 아직 어디 부분에 연결할지 정해주지 않았으므로 독립적으로 존재한다

print()

print('head.data:', head.data)  # >>> head는 1 즉, node1을 가리키고 있는 상황

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

print()

print('node.__dict__:', node.__dict__)
# >>> node.__dict__: {'data': 1, 'next': <__main__.Node object at 0x11030ffd0>}
# next에 들어있는 주소 (0x11030ffd0) 가 node의 포인터가 가리키는 데이터 (2)의 주소이다

print('node.next__dict__:', node.next.__dict__)
# >>> node.next__dict__: {'data': 2, 'next': <__main__.Node object at 0x11030fe50>}
# node.next에는 당연히 포인터가 가리키고 있는 노드의 데이터인 2가 들어있다


# 기존 node가 다음(next) 포인터로 가지고 있을 주소를 node_next에 저장한다
node_next = node.next

# 새로 만든 node3 인스턴스를 node.next에 할당한다
node.next = node3

# 기존 node가 가리키는 다음 포인터, node_next를 node3 인스턴스의 포인터로 할당한다
node3.next = node_next


print()

# head는 위에서 선언했던 node1 인스턴스를 가리킨다
node = head
while node.next:
    print(node.data)
    node = node.next
print('end of node.data:', node.data)

# 1
# 1.5
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# end of node.data: 9
