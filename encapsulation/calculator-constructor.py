class CalculatorCons:
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

if __name__ == '__main__':
    c = CalculatorCons(1, 2)
    print(c.add(), c.dev(), c.mul(), c.sub())


