class CalculatorStatic(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def dev(self):
        result = self.first / self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    @staticmethod
    def main():
        c = CalculatorStatic(int(input('첫번째 수 입력\n')), int(input('두번째 수 입력\n')))
        print(f'{c.first} + {c.second} = {c.add()}')
        print(f'{c.first} - {c.second} = {c.sub()}')
        print(f'{c.first} * {c.second} = {c.mul()}')
        print(f'{c.first} / {c.second} = {c.dev()}')
        print(c.add(), c.sub(), c.mul(), c.dev())


CalculatorStatic.main()