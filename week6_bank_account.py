class BankAccount:
    __monthly_interest_rate = 0.1
    
    def __init__(self,name, balance):
        self.__name = name
        self.__balance = balance
        
    def depositMoney(self, amount):
        self.__balance += amount
        
    def withdrawMoney(self, amount):
        if amount<= self.__balance :
            self.__balance -=amount
        
    def getBalance(self):
        return self.__balance
    
    def printAccountSummary(self):
        print(f'{self.__name} has {self.__balance} TL in account.')
        print(f'expected interest amount for a month is {str(self.__getExpectedMonthlyInterest())}')
        print('-'*20)
        
    def __getExpectedMonthlyInterest(self):
        return self.__balance * BankAccount.__monthly_interest_rate
    
account1 = BankAccount("ozan", 1000)
account2 = BankAccount("emre", 800)
account1.printAccountSummary()
account2.printAccountSummary()
account1.depositMoney(100)
account1.withdrawMoney(500)
account1.printAccountSummary()
account2.printAccountSummary()
