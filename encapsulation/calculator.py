def add_f(f, s):
    return f + s
def sub_f(f, s):
    return f - s
def mul_f(f, s):
    return f * s
def dev_f(f, s):
    return f / s


class Calculator:
    def __init__(self):
        pass

    def setdata(self, first, second):
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
    #c = Calculator()
    #c.setdata(1, 2)
    #print(c.add(), c.dev(), c.mul(), c.sub())
    print(add_f(1,2), sub_f(1,2), mul_f(1,2), dev_f(1,2))

