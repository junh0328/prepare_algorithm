# 2! = 2 * 1
# 3! = 3 * 2!
# 4! = 4 * 3!


def fibo(num):
    if num <= 1:
        return num

    return num * fibo(num-1)


print(fibo(4))
