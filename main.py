N, A = int(input()), {i: 1 for i in map(int, input().split())}

M = int(input())

print('A:', A)
# >>> A: {4: 1, 1: 1, 5: 1, 2: 1, 3: 1}

print('')

for i in list(map(int, input().split())):
    print(A.get(i, 0))
