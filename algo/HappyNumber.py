# def solution(n):
#     if n == 1:
#         return True
#     if n >= 10:
#         pass

#     return n // 10, n % 10, n


# Test code
# print(solution(1))  # True
# print(solution(19))  # True
# print(solution(61))  # False
# print(solution(201))  # False


def solution(n):
    r = s = 0
    while(n > 0):
        r = n % 10
        s += r**2
        n //= 10
    return s


n = int(input())
res = n

while(res != 1 and res != 4):
    res = solution(res)

if(res == 1):
    print("happy number")
elif(res == 4):
    print("not a happy number")
