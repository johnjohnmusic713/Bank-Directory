class Bank_Account:
    def __init__(self):
        self.balance=5000
        print("Hello & Welcome to the Deposit & Withdrawal Machine")
    def deposit(self):
        amount = float(input("Enter amount to be deposited : "))
        self.balance+=amount
        print("\n Amount Deposited : ",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn : "))
        if self.balance>=amount:5000
            self.balance-=amount
            print("\n You withdraw:",amount)
        else:
            print("\n Insufficient Balance ")
    def display(self):
        print("\n Net available balance=",self.balance)

s = Bank_Account()
s.deposit(5000)
s.withdraw(500)
s.display()
