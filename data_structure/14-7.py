# 추가 예제 코드
# search_from_head
# search_from_tail
# insert_before

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeManageMent:
    def __init__(self, data):
        # 인스턴스 초기화시에는 아직 연결된 노드들이 없으므로, head 와 tail 모두 인스턴스 본인을 가리키도록 만든다
        self.head = Node(data)
        self.tail = self.head

    # 맨 뒤 노드에 더블 링크드 리스트 추가
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            # 기존 head를 node 변수에 할당한다
            node = self.head
            # 링크드 리스트의 맨끝까지 도달하기 위함
            while node.next:
                node = node.next
            # 새로 추가할 data 객체를 new라는 변수에 할당
            new = Node(data)
            # 기존 링크드 리스트의 맨 마지막에 new를 링크 1(바인딩)
            node.next = new
            # 새로 추가할 data 객체의 앞에도 기존의 마지막 노드를 링크 2(바인딩)
            new.prev = node
            # 기존 링크드 리스트의 꼬리를 새로 추가할 data 객체로 바인딩
            self.tail = new

    def desc(self):
        # 어디서부터 내려올 지 기준을 잡는다
        # 기준은 head
        node = self.head
        while node.next:
            print('node.data:', node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False

        # node 변수를 통해 방향 명시
        node = self.head
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.tail == None:
            return False

        # node 변수를 통해 방향 명시
        node = self.tail
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.prev
        return False

    # data >> 삽입할 데이터
    # existing_data >>> 기존의 데이터
    # existing_data 앞에 data를 삽입할 것이다
    def insert_before(self, data, existing_data):
        if self.head == None:
            # head가 없을 경우, 노드 객체를 생성한다
            self.head = Node(data)
            return True
        # head가 있을 때
        else:
            # 맨 뒤에서부터 데이터를 검색한다
            node = self.tail
            while node.data != existing_data:
                # existing_data가 우리가 입력한 값과 맞을 때까지 앞으로 이동
                node = node.prev
                # 계속 앞으로 이동했을 때 결과가 None이라면 >>> data가 없는 것
                if node == None:
                    return False
            # while node.data == before_data: 일 경우, (data를 정상적으로 찾은 경우)
            # new라는 변수에 우리가 인수로 넣은 data를 객체화하여 할당
            # 양방향 링크드 리스트이므로 새로 추가할 변수를 기준으로 prev / / next 둘다 연결해줘야 함
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            # new.prev는 기존의 new (node.prev)를 가리켜야 한다
            new.prev = before_new
            new.next = node
            node.prev = new
            return True


node1 = NodeManageMent(1)

print('node1.__dict__:', node1.__dict__)

print()
print()

for elem in range(2, 11):
    node1.insert(elem)

node1.desc()

print()
print()

print(node1.search_from_head(2))

print()
print()

# data가 2 인 노드 앞에 1.5를 가지는 노드를 삽입할꺼야
node1.insert_before(1.5, 2)
node1.desc()
