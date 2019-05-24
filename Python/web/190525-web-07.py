#coding=utf-8

class Wallet:
    money = 0

    #처음 실행되는 메소드
    def __init__(self, name):
        print("{}님 환영합니다.".format(name))
        self.owner = name

    def __str__(self):
        return '{}의 지갑입니다.'.format(self.owner)

    def __repr__(self):
        return '{}의 지갑입니다.'.format(self)           

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
        
# sol_waller = Wallet('sol')
# suzy_waller = Wallet('suzy')

class Account(Wallet):
    def __init__(self, name, account_number):
        self.owner = name
        self.account_number = account_number
        super().__init__(name)

    def __str__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __repr__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __add__(self, another):
        return  self.money + another.money

    def __call__(self):
        print("호출되었습니다.")

    def send_moeny(self, money, to):
        if self.money > money:
            to.money += money
            self.money -= money
            print("{}원을 {}에게 보냈습니다.".format(money, to.owner))
            self.print_now_money()