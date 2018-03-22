class Account:
    def __init__(self):
        self.savings = 100
    def __init__(self):
        self.withdraw = 0

account1 = Account()
account1.savings = 400

account2 = Account()
account2.savings = 50

account3 = Account()
account3.savings = 1000

def withdraw(self, withdraw):
    withdraw = input("How much would you like to withdraw?")
    self.savings -= withdraw
    if self.savings < 0:
        print("Cannot withdraw that amount!")

def deposit(self, deposit):
    deposit = input

selectAccount = input("What account would you like to access?")
if selectAccount == "account1":
    print("Account 1 Selected")
    print("£" + (str(account1.savings)) + " Available to withdraw")
elif selectAccount == "account2":
    print("Account 2 Selected")
    print("£" + (str(account2.savings)) + " Available to withdraw")
elif selectAccount == "account3":
    print("Account 3 Selected")
    print("£" + (str(account3.savings)) + " Available to withdraw")
