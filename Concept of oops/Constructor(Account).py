class Account:

    def __init__(self, number, acc_type, balance):
        self.number = number
        self.acc_type = acc_type
        self.balance = balance

    def getNumber(self):
        return self.number

    def getAcc_type(self):
        return self.acc_type

    def getBalance(self):
        return self.balance


a = Account("Anshika","saving",35750)
print(a.getNumber())
print(a.getAcc_type())
print(a.getBalance())