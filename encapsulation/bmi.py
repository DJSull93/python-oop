class Bmi():
    def __init__(self, kg, msq):
        self.kg = kg
        self.msq = msq/100
    def get_bmi(self):
        score = self.kg / self.msq ** 2
        Bmi = ''
        if score >= 30:
            Bmi = '비만'
        elif 30 > score >=25:
            Bmi = '과체중'
        elif 25 > score >= 20:
            Bmi = '정상'
        else:
            Bmi = '저체중'
        return Bmi
    @staticmethod
    def main():
        c = Bmi(int(input('몸무게를 입력해주세요(kg)\n')), int(input('키를 입력해주세요(cm)\n')))
        print(f'BMI = {c.kg} kg / {c.msq} m^2 ')
        print(f'당신의 BMI는 {c.get_bmi()} 입니다')

Bmi.main()