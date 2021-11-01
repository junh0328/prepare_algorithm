# LinkedQueue() 라는 객체를 생성했지만, 사실 더블 링크드 리스트에 관한 문제이다

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front != None:
            return True
        elif self.rear != None:
            return True
        else:
            return False

    def put(self, data):
        if self.front == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            node = self.front
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.rear = new

    def get(self):
        pass

    def peek(self):
        node = self.front
        while node:
            if(node.data):
                print(node.data)
                break
            else:
                node = node.next


# Test code
queue = LinkedQueue()


# print(queue.is_empty())
for i in range(10):
    queue.put(i)
# print(queue.is_empty())


# for _ in range(11):
#     print(queue.get(), end=' ')
# print()

# for i in range(20):
#     queue.put(i)
# print(queue.is_empty())

for _ in range(5):
    print(queue.peek(), end=' ')
print()

# for _ in range(21):
#     print(queue.get(), end=' ')
# print()
# print(queue.is_empty())

# put(): Queue의 rear에 새로운 데이터를 입력한다. >>> insert_after
# 더블 링크드 리스트이므로, 연결할 때마다

# get(): Queue의 front에서 데이터를 반환한다. 출력한 데이터는 Queue에서 삭제한다. 더이상 출력할 데이터가 없는 경우 None을 반환한다.
# 삭제를 한다면 prev에서 또 빼고, next에서 또 빼야 겠군요

# peek(): Queue의 front에서 데이터를 반환한다. 반환한 데이터는 Queue에 그대로 유지한다. 반환할 데이터가 없는 경우 None을 반환한다.
