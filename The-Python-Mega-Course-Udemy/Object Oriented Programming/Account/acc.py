# from acc import Account
class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# account = Account("balance.txt")
# print(account.balance)
# account.withdraw(int(input("Enter the amount to be withdrawn: ")))
# print(account.balance)
# account.commit()

class Checking(Account):
    type = "checking"
    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
checking = Checking("balance.txt", 1)
checking.transfer(10)
print(checking.balance)
checking.commit()
