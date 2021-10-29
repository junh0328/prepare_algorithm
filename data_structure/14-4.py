# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeManagement:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print('data:', node.data, '/', 'next:', node.next)
            node = node.next


linkedList1 = NodeManagement(0)

print('linkedList1.__dict__:', linkedList1.__dict__)
# >>> linkedList1.__dict__: {'head': <__main__.Node object at 0x10a51b070>}

print('linkedList1.head:', linkedList1.head)
# >>> linkedList1.head: <__main__.Node object at 0x10a51b070>

print('linkedList1.head.data:', linkedList1.head.data)
# >>> linkedList1.head.data: 0

print('linkedList1.head.next:', linkedList1.head.next)
# >>> linkedList1.head.next: None

print()

for data in range(1, 11):
    linkedList1.add(data)

linkedList1.desc()
