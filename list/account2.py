import random

class Account(object):

    def __init__(self, acc_numb, name, money):
        self.BANK = 'SC은행'
        self.name = name
        self.acc_numb = acc_numb
        self.money = money

    @staticmethod
    def create_acc_numb():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    def to_string(self):
        return f'은행이름 : {self.BANK}\n' \
               f'이름 :{self.name}\n' \
               f'계좌번호 : {self.acc_numb}\n' \
               f'잔액 : {self.money}\n'

    @staticmethod
    def del_element(ls, acc_numb):
        for i, j in enumerate(ls):
            if j.acc_numb == acc_numb:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0. Exit, 1. Create, 2. Read, 3. deposit, 4. withdraw, 5. Delete' )
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(Account.create_acc_numb(), input('name'), input('money')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                acc_numb = input('수정할 계좌번호')
                money = input('입금액 입력바랍니다.')
                for i, j in enumerate(ls):
                    if j.acc_numb == acc_numb:
                        replace = Account(j.acc_numb, j.name,
                                          int(j.money)+int(money))
                        Account.del_element(ls, acc_numb)
                        ls.append(replace)
            elif menu == '4':
                acc_numb = input('수정할 계좌번호')
                money = input('출금액 입력바랍니다.')
                for i, j in enumerate(ls):
                    if j.acc_numb == acc_numb:
                        replace = Account(j.acc_numb, j.name,
                                          int(j.money)-int(money))
                        Account.del_element(ls, acc_numb)
                        ls.append(replace)
            elif menu == '5':
                Account.del_element(ls, input('삭제 계좌번호'))
            else:
                print('wrong Numb')
                continue

Account.main()