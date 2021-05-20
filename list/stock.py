class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_stock(self):
        return f'주식명 : {self.name}, 종목 코드 : {self.code}'

    @staticmethod
    def main():
        while 1:
            menu = input('1. 입력\n2. 출력\n0. 프로그램종료\n')
            if menu == '1':
                 c = Stock(input('주식명\n'), input('종목코드\n'))
            elif menu == '2':
                print(f'출력 결과 >> {c.get_stock()}')
            elif menu == '0':
                print('프로그램을 종료합니다.')
                break
            else:
                print('잘못된 결과입니다.')
                continue

Stock.main()