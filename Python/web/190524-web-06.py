#coding=utf-8

#with open('path', 'mode') as f: f = open()
    # f.write("안녕하세요. with 입니다")

# 자동으로 닫아줌.
# 파일 오픈 사용시 주로 사용함
# dir 함수로 무엇이 있는지 확인

# with open("./helloworld.txt", "r") as f:
#     print(f.read())

#파이썬 모듈(module)


# def add_all(*args):
#     return sum(args)


class Wallet:
    money = 0

    #처음 실행되는 메소드
    def __init__(self, name):
        self.owner = name

    def print_owner_name(self):
        print('owner name is', self.owner)

    def print_now_money(self):
        print("현재 잔액은: ", self.money)

    #돈을 지출
    def spend(self, m):
        if self.money < m:
            print("돈이 부족 합니다.")
            self.print_owner_name()
        else:
            self.money -= m
            print("{}를 지출 했습니다.".format(m))
            self.print_now_money()

    #돈을 추가
    def income(self, m):
        self.money += m
        self.print_now_money()
        
sol_waller = Wallet('sol')
suzy_waller = Wallet('suzy')
