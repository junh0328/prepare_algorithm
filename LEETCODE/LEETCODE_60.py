def solution(n, k):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i

    num = [i for i in range(1, n + 1)]
    res = [""] * (n)

    i = 0
    while k > 1:
        fact = fact//n
        idx = (k - 1)//fact
        k = k - (idx) * fact
        res[i] = num[idx]
        i += 1
        num.pop(idx)
        n -= 1
    for n in num:
        res[i] = n
        i += 1

    return res


print(solution(3, 3))
print(solution(4, 9))


# https://leetcode.com/problems/permutation-sequence/discuss/376990/Simply-Simple-Python-Solution-with-explanation-No-tricks-simple-math
