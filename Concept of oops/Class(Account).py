class account:
    number = None
    acc_type = None
    balance = None

    def setNumber(self,number):
        self.number = number

    def setacc_type(self,acc_type):
        self.acc_type = acc_type

    def setbalance(self,balance):
        self.balance = balance

    def getNumber(self):
        return self.number

    def getacc_type(self):
        return self.acc_type

    def getbalance(self):
        return self.balance

a = account()
a.setNumber("BOI7833388")
a.setacc_type("Saving")
a.setbalance(10500)
print(a.getNumber())
print(a.getacc_type())
print(a.getbalance())