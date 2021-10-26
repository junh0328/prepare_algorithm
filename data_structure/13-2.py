# 큐 (Queue)

import queue

# FIFO QUEUE (일반적인 구조의 큐) 사용하기

data_queue = queue.Queue()

# LIFO QUEUE (스택과 같은 구조의 큐) 사용하기

# data_queue = queue.LifoQueue()

print('data_queue:', data_queue)
print('type:', type(data_queue))

print()

# 데이터 삽입 (put)

data_queue.put(1)
data_queue.put(2)
data_queue.put(3)

print('data_queue.qsize():', data_queue.qsize())

print()

# 데이터 추출 (get)

print('data_queue.get():', data_queue.get())
print('data_queue.get():', data_queue.get())
print('data_queue.get():', data_queue.get())
