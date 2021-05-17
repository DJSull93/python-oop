class Bmi():
    def setBmi(self, kg, msq):
        self.kg = kg
        self.msq = msq
    def bbmi(self):
        result = self.kg / (self.msq * self.msq)
        return result

if __name__ == '__main__':
    c = Bmi()
    c.setBmi(72, 1.83)
    print(c.bbmi())
