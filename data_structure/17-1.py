# 이진 탐색 트리 삭제 코드 구현과 분석

# 1. 삭제할 Node 탐색
# 이를 위해 삭제할 Node가 없는 경우 False를 리턴하고, 함수를 종료시킴

# def delete(self, value)
# 실제로 받는 인자(value), self는 클래스의 메서드임을 나타내기 위해 씀
# 없으면 delete 할 필요가 없으므로 False 리턴

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
                print('go to left', self.current_node.value)
                self.current_node = self.current_node.left
            else:
                print('go to right', self.current_node.value)
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        # 트리를 순회하면서 값을 찾았는지 확인
        # 해당 값을 가지는 트리의 노드가 있을 경우, True로 변경
        # self.current_node >>> 삭제할 노드
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            # 삭제할 노드와 입력한 value값과 같다면 searched를 true로 변경
            if self.current_node == value:
                searched = True
                break
            # 왼쪽으로 갈 경우
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            # 오른쪽으로 갈 경우 (value가 같거나 클 경우)
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        # while문을 다 통과했을 경우
        # 1 searched가 true 이며
        # 2 self.current_node >>> 삭제할 노드
        # 3 self.parent >>> 삭제할 노드의 부모 노드

        # 만약 searched가 false이면, 삭제하고자 입력한 노드가 트리안에 없는 것이다
        # 따라서 False를 리턴한다

        if searched == False:
            return False

        # 이후부터 Case (3가지)들을 분리해서 코드 작성
        # 1. Leaf Node 삭제 (본인 삭제, 자식 노드가 없음)
        # 2. Node 삭제 (child node가 1개 있을 경우)
        # 3. Node 삭제 (child node가 2개 있을 경우)

        # case 1: Leaf Node 삭제 (본인 삭제, 자식 노드가 없음)
        # self.current_node가 삭제할 노드, self.parent는 삭제할 노드의 부모 노드
        # 본인 노드를 기준으로 왼쪽과 오른쪽 자녀거 모두 없는 경우이다

        if self.current_node.left == None and self.current_node.right == None:
            # 삭제하려는 value가 부모 노드보다 작으면 왼쪽/ 크면 오른쪽이겠죠?
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            # 메모리 상에서도 삭제하기
            del self.current_node

        # case 2: Node 삭제 (child node가 1개 있을 경우)
        # child가 1개인데, 왼쪽에 있을 수도 있고, 오른쪽에 있을 수도 있다

        # 자식 노드가 본인 기준 왼쪽에 있을 때
        if self.current_node.left != None and self.current_node.rigth == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.right
        # 자식 노드가 본인 기준 오른쪽에 있을 때
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # case 3:
        if self.current_node.left != None and self.current_node.right != None:  # case3
            if value < self.parent.value:  # case3-1
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # 16을 기준으로 17이 존재하면 18의 왼쪽(left)에 17을 붙여야 한다
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                # self.change_node.right == None: 일 경우
                else:
                    self.change_node_parent.left = None
                # while문 순회를 마친 뒤, 16을 current_node인 15 대신 삽입하려는 경우
                # 31의 왼쪽에 16을 연결
                self.parent.left = self.change_node
                # 16의 오른쪽에 (15가 가지고 있던 자식 노드의 오른쪽)18을 연결
                # 16의 왼쪽에 (15가 가지고 있던 자식 노드의 왼쪽) 13을 연결
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            else:
                self.change_node = self.current_node.right  # (18)
                self.change_node_parent = self.current_node.right  # (18)
                while self.change_node.left != None:  # (18)의 왼쪽 자식이 있다면
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # while 반목문을 전부 순회한 경우
                # change_node_parent 자리에는 18이
                # change_node 자리에는 16이 설정된다

                # 16의 오른쪽에 값이 있다면?
                # 18의 왼쪽에 17을 연결한다 why? 16은 15(current_node)를 대체할 예정이므로
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                # 16의 오른쪽에 값이 없다면?
                # 18의 왼쪽 자녀의 값을 비워둔다
                else:
                    self.change_node_parent.left = None
                # change_node_parent와 change_node 자리의 구성이 완료된 상태
                # current_node를 제거하고 change_node를 parent의 right에 붙인다
                # change_node의 왼쪽에는 기존에 current_node가 가졌던 left를 붙이고
                # change_node의 오른쪽에는 while문을 통해 변경한
                # change_node_parent인 cureent_node.right를 붙인다
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
