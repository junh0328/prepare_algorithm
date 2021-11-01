class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def preorder(self):
        self.current_node = self.root
        # print(self.root.__dict__)
        while self.current_node:
            if self.current_node.left:
                print('left:', self.current_node.left.data)
                if self.current_node.left.left:
                    self.current_node.left = self.current_node.left.left
                else:
                    self.current_node.left = self.current_node.left.right
            elif self.current_node.right:
                print('right:', self.current_node.right.data)
                if self.current_node.right.left:
                    self.current_node.right = self.current_node.right.left
                elif self.current_node.right.right:
                    self.current_node.right = self.current_node.right.right
                else:
                    return False
            else:
                return False
        return False


# Test code
root = Node(5, Node(2, Node(7, Node(4), Node(1)),
            Node(3)), Node(9, Node(6), Node(10)))
tree = Tree(root)

tree.preorder()


# {'data': 5, 'left': <__main__.Node object at 0x1048afca0>, 'right': <__main__.Node object at 0x1048afb80>}

# print('tree.root.__dict__', tree.root.__dict__)
# # tree.root.__dict__ {'data': 5, 'left': <__main__.Node object at 0x10e753c70>, 'right': <__main__.Node object at 0x10e753b50>}

# print()

# # 왼쪽

# print('tree.root.left.__dict__:', tree.root.left.__dict__)

# print()

# print('tree.root.left.left.__dict__:', tree.root.left.left.__dict__)

# print()

# print('tree.root.left.left.left__dict__:', tree.root.left.left.left.__dict__)

# print()

# print('tree.root.left.left.right.__dict__:',
#       tree.root.left.left.right.__dict__)

# print()

# print('tree.root.left.right.__dict__:', tree.root.left.right.__dict__)

# print()

# # 오른쪽

# print('tree.root.right.__dict__:', tree.root.right.__dict__)

# print('tree.root.right.left.__dict__:', tree.root.right.left.__dict__)

# print('tree.root.right.right.__dict__:', tree.root.right.right.__dict__)

# # preorder

# # root node 부터 순회를 시작한다
# # while 문을 통해 반복한다

# # 새로운 노드에 접근할 경우
# # 1. Node에 있는 data를 출력한다 >>> print
# # 2. Node에 left child가 있으면, left child node에 접근한다
# # 3. Node에 right child가 있으면, right child node에 접근한다

# # root node에서 순회흘 시작할 경우, 재귀적 동작으로 인해 모든 node의 data를 출력할 수 있다

#           5

#       2       9

#   7     3   6   10

# 4   1
