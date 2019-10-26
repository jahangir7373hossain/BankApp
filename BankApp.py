import sys


class Customer:
    bankName = "Bangladesh Bank"
    username = ['Jahangir', 'Hossain', 'Khan']
    password = [1234, 5678, 9101]

    def __init__(self, balance=0):
        self.balance = balance

    def user(self, customerUsername):
        for user in Customer.username:
            if user == customerUsername:
                print("User name is correct")
                break
        else:
            print("User name is not correct")
            sys.exit()

    def passw(self, customerPassword):
        for password in Customer.password:
            if password == customerPassword:
                print("Your password is correct")
                break
        else:
            print("password is not correct")
            sys.exit()

    def deposite(self,amount):
        self.balance = self.balance + amount
        print("After deposit total balance is: ", self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient fund can not perform this operation")
            sys.exit()
        self.balance = self.balance - amount
        print("After withdraw the balance is: ", self.balance)


print("Welcome to", Customer.bankName)

c = Customer(10)
usrN = input("Enter user name: ")
c.user(usrN)
passWord = float(input("Enter password: "))
c.passw(passWord)
print("Logged in successfully")
while True:
    print("d-Deposit\nw-Withdraw\ne-Exit")
    option = input("Choose your option")
    if option.lower() == 'd':
        amt = float(input("Enter the amount: "))
        c.deposite(amt)
    if option.lower() == 'w':
        amt = float(input("Enter the amount: "))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
        print('Thanks for Banking')
        sys.exit()
    else:
        print("Please choose valid option")



