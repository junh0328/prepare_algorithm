# 피보나치 수열을 계산하기 위한 모듈

class Fibonacci:
    def __init__(self, title='fibonacci'):
        self.title = title

    def fibo(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fibo2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result
