class Mortgage:
    def __init__(self, amount, maturity, interest):
        self.amount = amount
        self.maturity = maturity
        self.__interest = interest
    
    def get_interest(self):
        return self.__interest
    
    def set_interest(self, newInterest):
        if newInterest >= 0:
            self.__interest = newInterest
        else:
            print('Interest must be non-negative!')

    def __str__(self):
        return f'This is a {self.maturity} year long mortgage, with a principal of {self.amount} and an interest rate of {self.interest}%'

    def payment(self):
        B = self.amount
        n = self.maturity*12
        r = self.__interest/100

        return B*(r*(1+r)**n)/((1+r)**n-1)
        

m = Mortgage(100000, 30, 6)

m.payment()

print(m)