class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    # 초기화
    def __init__(self, data):
        # 기존과 같이 앞에서부터 검색하기 위함
        self.head = Node(data)
        # 뒤에서부터 검색하기 위함
        self.tail = self.head

    # 삽입하기
    # node.next 맨 뒤에 특정 노드를 생성한 후, 기존 링크드 리스트와 연결하는 메서드이다
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    # 출력하기
    def desc(self):
        node = self.head
        while node:
            print('node.prev:', node.prev)
            print('node.data:', node.data)
            print('node.next:', node.next)
            print()
            node = node.next
