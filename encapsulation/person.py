'''
이름, 출생년도, 주소를 입력받아서
2000년생 회원가입한 사람의 이름, 나이(만), 주소를 출력하시오
'''
class Person(object):
    def __init__(self, name, age, add):
        self.name = name
        self.age = 2021 - age
        self.add = add
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_add(self):
        return  self.add
    @staticmethod
    def main():
        c = Person(str(input(f'이름을 입력하세요\n')), int(input(f'출생년도를 입력하세요\n')), str(input(f'주소를 입력하세요\n')))
        print(f'이름 : {c.get_name()}')
        print(f'나이 : {c.get_age()}')
        print(f'주소 : {c.get_add()}')

Person.main()

