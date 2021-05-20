class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_stock(self):
        return f'주식명 : {self.name}, 종목 코드 : {self.code}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('1. 입력\n2. 출력\n3. 수정\n4. 삭제\n0. 프로그램종료\n')
            if menu == '1':
                 ls.append(Stock(input('주식명\n'), input('종목코드\n')))
            elif menu == '2':
                for i in ls:
                    print(f'출력 결과 >> {i.get_stock()}')
            elif menu == '3':
                edit_name = input('수정할 종목')
                edit_info = Stock(edit_name, input('수정할 코드'))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)
            elif menu == '4':
                del_name = input('삭제할 종목')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif menu == '0':
                print('프로그램을 종료합니다.')
                break
            else:
                print('잘못된 결과입니다.')
                continue

Stock.main()