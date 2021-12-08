# https://pythontutor.com/visualize.html#mode=edit

def dfs(graph, v, visited):
  visited[v] = True
  # print(v, end=' ')
  for i in graph[v]:
    print('i:', i, graph[v], 'v:',v)
    print('')
    if not visited[i]: # if not visited[i] 가 무슨 말임? False 라는 의미인가? >>> i 가 False일 때 재귀로 반복해라
      print('not visited[i]:', i, visited[i])
      dfs(graph, i, visited)
      print('')

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited = [False] * 9 

# print('visited:', visited)
# >>> visited: [False, False, False, False, False, False, False, False, False]

dfs(graph, 1, visited)


# i: 2 [2, 3, 8] v: 1
# i: 1 [1, 7] v: 2
# i: 7 [1, 7] v: 2
# i: 2 [2, 6, 8] v: 7
# i: 6 [2, 6, 8] v: 7
# i: 7 [7] v: 6

# i: 8 [2, 6, 8] v: 7
# i: 1 [1, 7] v: 8
# i: 7 [1, 7] v: 8



# i: 3 [2, 3, 8] v: 1
# i: 1 [1, 4, 5] v: 3
# i: 4 [1, 4, 5] v: 3
# i: 3 [3, 5] v: 4
# i: 5 [3, 5] v: 4
# i: 3 [3, 4] v: 5
# i: 4 [3, 4] v: 5


# i: 5 [1, 4, 5] v: 3

# i: 8 [2, 3, 8] v: 1