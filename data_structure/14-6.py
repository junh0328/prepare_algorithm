# 더블 링크드 리스트
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeManagement:
    # 초기화
    def __init__(self, data):
        # 기존과 같이 앞에서부터 검색하기 위함
        self.head = Node(data)
        print('self.head:', self.head.__dict__)
        # 뒤에서부터 검색하기 위함
        # 현재 기본 값으로는 self.tail = Node(data) 와 같은 의미이다
        # 데이터가 하나일 경우에는 처음이나 끝이나 모두 같은 주소를 가리키고 있기 때문
        self.tail = self.head
        print('self.tail:', self.tail.__dict__)

    # 삽입하기
    # node.next 맨 뒤에 특정 노드를 생성한 후, 기존 링크드 리스트와 연결하는 메서드이다
    def insert(self, data):
        # 방어 코드이다.
        # 사실 인스턴스를 생성할 때 head 와 tail은 초기화 단계에서 무조건 값이 들어 있다
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        # head가 있는 경우, 실질적인 코드이다
        # 추가하면서 인수로 받는 새로운 데이터(data)를 head로 설정된 인스턴스 내부의 데이터와 연결시켜야 한다
        else:
            # 인스턴스의 현재 head를 node라는 변수에 할당한다
            node = self.head
            # while 문이 true라는 것은 해당 노드의 다음 노드가 존재한다는 것을 의미한다
            while node.next:
                node = node.next
            # 추가로 받는 data를 객체 형식으로 만들어 new라는 변수에 할당한다
            # new는 insert된 data로, 새롭게 연결해야 할 노드이다
            new = Node(data)
            # node(=self.head)의 다음번(next)이라는 속성에 앞서 만든 new 변수의 데이터를 할당한다
            node.next = new
            # 새로 만든 노드도 자신의 앞에 있는 노드의 메모리 주소를 가지고 있어야 한다
            # 또한, 더블 링크드 리스트이므로 새로 만든 변수 앞에는 기존 head를 삽입한다
            new.prev = node
            # 꼬리에는 객체형식의 새로운 data (new = Node(data))를 할당한다
            self.tail = new

    # 출력하기
    def desc(self):
        node = self.head
        print('self.head is:', self.head.__dict__)
        # >>> self.head is: {'prev': None, 'data': 1, 'next': <__main__.Node object at 0x109847e20>}
        while node:
            print('node.prev:', node.prev)
            print('node.data:', node.data)
            print('node.next:', node.next)
            print()
            node = node.next


node1 = NodeManagement(1)

for index in range(2, 11):
    node1.insert(index)

node1.desc()

# node.prev: None
# node.data: 1
# node.next: <__main__.Node object at 0x10e443e20>
#
# node.prev: <__main__.Node object at 0x10e443eb0>
# node.data: 2
# node.next: <__main__.Node object at 0x10e443d90>
#
# node.prev: <__main__.Node object at 0x10e443e20>
# node.data: 3
# node.next: <__main__.Node object at 0x10e443d30>
#
# node.prev: <__main__.Node object at 0x10e443d90>
# node.data: 4
# node.next: <__main__.Node object at 0x10e443cd0>
#
# node.prev: <__main__.Node object at 0x10e443d30>
# node.data: 5
# node.next: <__main__.Node object at 0x10e443c70>
#
# node.prev: <__main__.Node object at 0x10e443cd0>
# node.data: 6
# node.next: <__main__.Node object at 0x10e443c10>
#
# node.prev: <__main__.Node object at 0x10e443c70>
# node.data: 7
# node.next: <__main__.Node object at 0x10e443bb0>
#
# node.prev: <__main__.Node object at 0x10e443c10>
# node.data: 8
# node.next: <__main__.Node object at 0x10e443b50>
#
# node.prev: <__main__.Node object at 0x10e443bb0>
# node.data: 9
# node.next: <__main__.Node object at 0x10e443af0>
#
# node.prev: <__main__.Node object at 0x10e443b50>
# node.data: 10
# node.next: None
