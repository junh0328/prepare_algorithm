# 주석 코드

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            # 입력한 value보다 사전에 초기화된 self.head의 value가 더 클 경우 (왼쪽으로 가야겠죠?)
            if value < self.current_node.value:
                # 왼쪽으로 갔는데, self.head의 오른쪽에 데이터가 있다면 (None이 아니라면)?
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                # 왼쪽으로 갔는데, self.head의 오른쪽에 데이터가 없다면 (Nonde 이라면)?
                else:
                    self.current_node.left = Node(value)
                    break
            # 입력한 value가 self.head.value보다 클 경우 (오른쪽으로 가야겠죠?)
            # 같을 경우에도 오른쪽으로 가게 처리했다
            else:
                if self.current_node.right != None:
                    # self.current_node(=self.head) 헤드를 self.current_node.right로 바꿔줘라
                    self.current_node = self.current_node.right
                else:
                    # right에 새로운 Node(value)를 붙여주고 종료해라
                    self.current_node.right = Node(value)
                    break

    # ---- insert까지는 위와 동일한 코드이다 ----
    # 데이터의 여부를 파악하기 때문에, True <-> False를 반환한다

    def search(self, value):
        # self.current_node 라는 변수를 통해 self.head를 할당한 후 어디서부터 순회할지 결정한다
        # 순회할 기준은 처음 head로 설정한 값이겠죠?
        self.current_node = self.head
        while self.current_node:
            # 현재 self.current_node의 value가 내가 찾고자하는 value라면 True를 반환한다
            if self.current_node.value == value:
                print('find value:', value)
                return True
            # 내가 찾고자하는 value가 self.current_node의 value보다 작을 경우 (왼쪽)
            elif value < self.current_node.value:
                print('go to left')
                self.current_node = self.current_node.left
            # 내가 찾고자하는 value가 self.current_node의 value보다 클 경우 (오른쪽)
            else:
                # 같을 경우도 오른쪽으로 이동한다
                print('go to right')
                self.current_node = self.current_node.right
        # 순회했을 때 없을 경우에는 False를 반환한다
        return False


head = Node(1)
BST = NodeMgmt(head)

print('head.value:', BST.head.value)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(8))
