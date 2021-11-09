def solution(a):
    match = ''
    stack = list()
    # print(a)
    for index in range(len(a)):
        left, right = '', ''
        # stack이 비어있을 경우 일단 문자열 하나를 추가한다
        if len(stack) == 0:
            stack.append(a[index])
        else:
            # left > 스택에 들어있던 문자열
            # right > 스택에 넣으려고 했던 문자열
            left = stack.pop()
            right = a[index]
            for i in range(len(left)):
                if left[i] in right:
                    match += left[i]

            for i in range(len(match)):
                if match[i] not in stack:
                    stack.append(match[i])

    stack = "".join(stack)
    return len(stack)


print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg']))
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg']))  # 0
