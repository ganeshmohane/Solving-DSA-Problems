class ATM:
    def __init__(self):
        self.balance = 0

    def deposit(self,balance):
        self.balance = balance
        return self.balance
        #pass
    def withdraw(self,amount):
        print("balance",self.balance)
        if amount >= self.balance:
            self.amount = self.balance - amount
            return self.amount
        else :
            return f"Your Balance is insufficient"
    def check_balance(self):
        return self.balance
        #pass

print("Welcome to Gforgenuis Bank ")
print()
while True:
    atm = ATM()
    print()
    print("Plz select the operation : ")
    choice = int(input("1.View Balance\n2.Add Money\n3.Withdraw Money\n "))
    if choice == 1:
        balance = atm.check_balance()
        print("Your Balance is",float(balance),"$")
    elif choice == 2:
        amount = int(input("Enter Amount to Deposit : \n"))
        deposit = atm.deposit(amount)
        balance = atm.check_balance()
        print("Your Balance is",float(balance),"$")
    elif choice == 3:
        amount = int(input("Enter Amount to Withdraw : \n"))
        withdraw = atm.withdraw(amount)
        print("withdraw",withdraw)
        balance = atm.check_balance()
        print("Your Balance is",float(balance),"$")
    else :
        exit()



print(deposit,balance, withdraw)
