import random
class Account(object):
    def __init__(self, name, deposit):
        self.bank = 'SC은행'
        self.name = name
        rls = list(range(10))
        self.code = f'{random.sample(rls,3)}-{random.sample(rls,2)}-{random.sample(rls,6)}'
        self.deposit = deposit
    def get_account(self):
        return f'은행 : {self.bank}\n예금주 : {self.name}\n계좌번호 : {self.code}\n잔액 : {self.deposit}'

    @staticmethod
    def main():
        while 1:
            menu = input('1. 입력 2. 출력 0. 종료\n')
            if menu == '1':
                c = Account(input('이름'), input('입금액'))
            elif menu == '2':
                print(f'{c.get_account()}')
            elif menu == '0':
                print('프로그램을 종료합니다.')
                break
            else:
                print('잘못된 접근입니다.')
                continue
Account.main()