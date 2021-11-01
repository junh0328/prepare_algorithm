# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeManagement:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                print('find Value:', value)
                return True
            elif value < self.current_node.value:
                print('go to left', value)
                self.current_node = self.current_node.left
            else:
                print('go to right', value)
                self.current_node = self.current_node.right
        return False


head = Node(1)
BST = NodeManagement(head)

BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(8))
