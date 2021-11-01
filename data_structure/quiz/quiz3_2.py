class Stack:
    def __init__(self):
        self.list = list()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()


class Calculator:
    def __init__(self):
        self.stack = Stack()

    def calculate(self, string):
        self.stack.list = []
        string = string.replace(" ", "")
        lt = 0
        rt = 0
        for elem in string:
            if elem.isnumeric() == True:
                self.stack.push(elem)
            else:
                rt = int(self.stack.pop())
                lt = int(self.stack.pop())
                if elem == '+':
                    self.stack.push(lt+rt)
                elif elem == '*':
                    self.stack.push(lt*rt)
                elif elem == '/':
                    self.stack.push(int(lt/rt))
                elif elem == '-':
                    self.stack.push(lt-rt)
                else:
                    return False

        return self.stack.list[0]


# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))

# 0. 문자열의 공백을 제거한다
# 1. 문자열을 stack에 담는다.
# 2. 들어오는 문자열이 숫자가 아닐 경우 pop 한다
# 3. 먼저 pop된 문자를 rt, 후에 pop된 문자를 lt에 할당한다
# 4. 숫자가 아닌 문자(연산자)를 바탕으로 lt 와 rt를 더한다
# 5. 다시 스택에 집어넣는다

# 2 > 3 > 4 > 5 를 반복한다
