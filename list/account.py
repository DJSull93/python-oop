import random

class Account(object):

    def __init__(self, name, deposit):
        self.BANK = 'SC은행'
        self.name = name
        rls = list(range(10))
        self.code = self.create_acc_numb()
        self.deposit = deposit
    def get_account(self):
        return f'은행 : {self.BANK}\n예금주 : {self.name}\n계좌번호 : {self.code}\n잔액 : {self.deposit}'
    def create_acc_numb(self):
        ls = []
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('1. 입력 2. 출력 3. 계좌 삭제 0. 종료\n')
            if menu == '1':
                ls.append(Account(input('이름'), input('입금액')))
            elif menu == '2':
                for i in ls:
                    print(f'{i.get_account()}')
            elif menu == '3':
                del_name = input('예금주명')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif menu == '0':
                print('프로그램을 종료합니다.')
                break
            else:
                print('잘못된 접근입니다.')
                continue
Account.main()