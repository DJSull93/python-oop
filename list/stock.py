class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_string(self):
        return f'주식명 : {self.name}, 종목 코드 : {self.code}'

    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('1. 입력\n2. 출력\n3. 수정\n4. 삭제\n0. 프로그램종료\n')
            if menu == '1':
                ls.append(Stock(input('주식명\n'), input('종목코드\n')))
            elif menu == '2':
                for i in ls:
                    print(f'출력 결과 >> {i.to_string()}')
            elif menu == '3':
                code = input('수정할 종목')
                stock = Stock(code, input('수정할 코드'))
                stock.del_element(ls, code)
                ls.append(stock)
            elif menu == '4':
                stock = Stock(None, input('삭제할 코드'))
                stock.del_element(ls, stock.code)
            elif menu == '0':
                print('프로그램을 종료합니다.')
                break
            else:
                print('잘못된 결과입니다.')
                continue

Stock.main()