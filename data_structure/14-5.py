# 링크드 리스트의 복잡한 기능2 (특정 노드를 삭제)

# 노드를 삭제하는 경우는 크게 3가지로 볼 수 있다

# 1. head 삭제
# 2. 마지막 노드 삭제
# 3. 중간 노드 삭제

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# NodeManagement 클래스를 통해 인스턴스를 생성할 경우
# 자동으로 해당 data를 가진 변수가 head(우리가 정한 제일 앞에 있는 리스트)가 된다


class NodeManagement:
    def __init__(self, data):
        # Node 클래스에 해당 data를 넣어주고, 이렇게 만든 인스턴스를 head로 만든다
        self.head = Node(data)
        print('initialize self.head:', self.head)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            # 헤더로 선택된 노드의 next가 None이 될 때까지 (node.next가 있을 때까지)
            while node.next:
                # 다음 노드와 헤더를 연결해준다
                node = node.next
            # 다음 노드에 데이터를 추가한다
            node.next = Node(data)
            print('node:', node.__dict__)
            print('next:', node.next)
            print()

    def desc(self):
        node = self.head
        while node:
            print('node.data:', node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print('해당 값을 가진 노드가 없습니다.')
            return

        # head (제일 선행 노드)를 삭제하는 경우
        # >>> 그 다음 노드(node.next)를 head로 만들어줘야 한다

        # 너가 삭제하려고 입력한 data가 head(제일 선행)의 data와 같니?
        if self.head.data == data:
            # 선행 데이터의 head를 임시 temp 변수에 저장
            temp = self.head
            # 선행 데이터의 다음 데이터를 기존 선행 데이터에 재할당
            self.head = self.head.next
            # 기존 선행 데이터의 head 삭제
            del temp

        # 중간 또는 맨뒤의 노드를 삭제하려는 경우
        # 너가 삭제하려고 입력한 data가 head(제일 선행)의 data와 다르니?
        else:
            # node라는 변수에 선행 데이터를 저장
            node = self.head
            # 헤더로 선택된 노드의 next가 None이 될 때까지 (node.next가 있을 때까지)
            while node.next:
                # 중간 노드를 삭제하는 경우
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    print('node.next.__dict__:', node.next.__dict__)
                    print('node.next.next.__dict__:', node.next.next.__dict__)
                    print('temp.__dict__:', temp.__dict__)
                    del temp
                    return
                else:
                    node = node.next


node1 = NodeManagement(1)

print()
print()

print('node1.__dict__:', node1.__dict__)
# >>> node1.__dict__: {'head': <__main__.Node object at 0x10270be80>}
print('node1.head.data:', node1.head.data)
# >>> node1.head.data: 1
print('node1.head.next:', node1.head.next)
# >>> node1.head.next: None

print()
print()

for item in range(2, 11):
    node1.add(item)

# node: {'data': 1, 'next': <__main__.Node object at 0x1019f3df0>}
# next: <__main__.Node object at 0x1019f3df0>
#
# node: {'data': 2, 'next': <__main__.Node object at 0x1019f3d60>}
# next: <__main__.Node object at 0x1019f3d60>
#
# node: {'data': 3, 'next': <__main__.Node object at 0x1019f3d00>}
# next: <__main__.Node object at 0x1019f3d00>
#
# node: {'data': 4, 'next': <__main__.Node object at 0x1019f3ca0>}
# next: <__main__.Node object at 0x1019f3ca0>
#
# node: {'data': 5, 'next': <__main__.Node object at 0x1019f3c40>}
# next: <__main__.Node object at 0x1019f3c40>
#
# node: {'data': 6, 'next': <__main__.Node object at 0x1019f3be0>}
# next: <__main__.Node object at 0x1019f3be0>
#
# node: {'data': 7, 'next': <__main__.Node object at 0x1019f3b80>}
# next: <__main__.Node object at 0x1019f3b80>
#
# node: {'data': 8, 'next': <__main__.Node object at 0x1019f3b20>}
# next: <__main__.Node object at 0x1019f3b20>
#
# node: {'data': 9, 'next': <__main__.Node object at 0x1019f3ac0>}
# next: <__main__.Node object at 0x1019f3ac0>

node1.desc()

# node.data: 1
# node.data: 2
# node.data: 3
# node.data: 4
# node.data: 5
# node.data: 6
# node.data: 7
# node.data: 8
# node.data: 9
# node.data: 10

print()
print()

node1.delete(3)
# node.next.__dict__: {'data': 4, 'next': <__main__.Node object at 0x1101cfc70>}
# node.next.next.__dict__: {'data': 5, 'next': <__main__.Node object at 0x1101cfc10>}
# temp.__dict__: {'data': 3, 'next': <__main__.Node object at 0x1101cfcd0>}

print()
print()

node1.desc()

# node.data: 1
# node.data: 2
# node.data: 4
# node.data: 5
# node.data: 6
# node.data: 7
# node.data: 8
# node.data: 9
# node.data: 10
