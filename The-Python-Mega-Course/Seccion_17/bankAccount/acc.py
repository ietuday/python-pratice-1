class Account:
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance-=amount
            self.commit()
        else:
            print("Insufficient funds")

    def deposit(self,amount):
        self.balance+=amount
        self.commit()

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    '''This class generates checking account objects'''
    type = "checking"

    def __init__(self,filepath,fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance= self.balance -amount - self.fee
        self.commit()


#account  = Account("balance.txt")
checking = Checking("balance.txt",1)
print(checking.__doc__)
