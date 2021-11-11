def gcdString(A: str, B: str):
    # A가 더 클 경우
    # A를 기준으로 B를 순회하여 해당하는 값이 있는지 체크
    if len(A) > len(B):
        for index in range(len(B)):
            if B[index] in A:
                print(B[index])
            else:
                return ''
    # B가 더 클 경우
    # B를 기준으로 A를 순회하여 해당하는 값이 있는지 체크
    else:
        for index in range(len(A)):
            if A[index] in B:
                print(A[index])
            else:
                return ''
    print()


gcdString('str', 'st')

gcdString('str', 'string')

gcdString('fast', 'str')
