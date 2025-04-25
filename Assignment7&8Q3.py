class Account:
    def __init__ (self,bal,accNo):
        self.balance = bal
        self.account = accNo

    def debit(self,amount):
        self.amount = amount
        self.balance -= amount
        print("Rs",amount,"was debited from account.")
        print("Total amount in account : Rs ",acc1.getBalance(),"\n Transaction Successful")

    def credit(self,amount):
        self.amount = amount
        self.balance += amount
        print("Rs",amount,"was added to the account")
        print("Total amount in account : ",acc1.getBalance(),"\n Transaction Successful")

    def getBalance(self):
        return self.balance
    
acc1 = Account(100000,99463327)
print("--Good evening Account number : ",acc1.account,"\n --Your bank balance is : Rs",acc1.balance)
print(acc1.credit(10000))
print(acc1.debit(5000))
print(acc1.credit(6000))

acc2 = Account(400000,12345)
print("--Good evening Account number : ",acc2.account,"\n --Your bank balance is : Rs",acc2.balance)
print(acc1.credit(6000))
print(acc1.debit(20000))
print(acc1.credit(12000))