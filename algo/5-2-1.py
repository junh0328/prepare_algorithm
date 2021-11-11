def gcdString(A: str, B: str):
    if len(A) < len(B):
        return gcdString(B, A)

    if B[0] == '':
        return A

    if A not in B:
        return ''

    A = A.replace(B, '')
    return gcdString(B, A)


print(gcdString('aba', 'ab'))
