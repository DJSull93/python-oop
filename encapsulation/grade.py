class Grade:
    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat
    def sum(self):
        return  self.kor + self.eng + self.mat
    def avg(self):
        return  int(self.sum()/3)
    def get_grade(self):
        score = int(self.avg())
        grade = ''
        if score >= 90:
            grade = 'A학점'
        elif 90 > score >= 80:
            grade = 'B학점'
        elif 80 > score >= 70:
            grade = 'C학점'
        elif 70 > score >= 60:
            grade = 'D학점'
        else:
            grade = 'F학점'
        return  grade

    @staticmethod
    def main():
        c = Grade(int(input('국어 점수\n: ')), int(input('영어 점수\n: ')), int(input('수학 점수\n: ')))
        print(f'총점: {c.sum()}, 평균 {c.avg()}, 학점 {c.get_grade()}')

Grade.main()

