# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #이름 숨김(__추가)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000) 
account1.deposit(5000) #추가
account1.withdraw(3000)
#account1.balance = 15000000 #보이면 안되는데?
print(account1)
#print(account1.__balance) #숨김처리 되어있어서 에러가 뜸

#이름변경(_BankAccount__balance)
#백도어(테스트하는 용도)
#print(account1._BankAccount__balance)