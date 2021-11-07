def function(data: str):
    A = list()
    C = list(data)
    for index in range(len(data)):
        A.append(data[index])
    if C == A[::-1]:
        print('true')
    else:
        print('false')


function('motor')
