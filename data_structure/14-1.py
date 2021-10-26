# 스택 (Stack)

# 큐와 달리 파이썬, JS 에서 기본 제공하는 리스트를 통해서 구현이 가능하다
# 큐의 경우 data = queue.Queue() 와 같이 인스턴스로 만들어서 사용했었음

# append: 삽입하기 (push)
# pop: 꺼내기 (pop)

data_stack = list()

data_stack.append(1)
data_stack.append(2)

print('data_stack:', data_stack)

print()

data_stack.pop()

print('① data_stack.pop():', data_stack)

print()

data_stack.pop()

print('② data_stack.pop():', data_stack)
