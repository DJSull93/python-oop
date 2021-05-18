class GradeCons:
    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat
    def sum(self):
        result = self.kor + self.eng + self.mat
        return result
    def avg(self):
        result = round(self.sum()/3)
        return result
if __name__ == '__main__':
    c = GradeCons(32, 45, 62)
    print(c.sum(), c.avg())
