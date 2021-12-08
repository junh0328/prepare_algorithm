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

for i in range(len(graph)):
  print('')
  for j in graph[i]:
    print('i:', i, "j:", j)

# i: 1 j: 2
# i: 1 j: 3
# i: 1 j: 8

# i: 2 j: 1
# i: 2 j: 7

# i: 3 j: 1
# i: 3 j: 4
# i: 3 j: 5

# i: 4 j: 3
# i: 4 j: 5

# i: 5 j: 3
# i: 5 j: 4

# i: 6 j: 7

# i: 7 j: 2
# i: 7 j: 6
# i: 7 j: 8

# i: 8 j: 1
# i: 8 j: 7