class BankingSystem:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0 :
            raise ValueError('The Amount Must Be Positve')
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('You Dont Have Enough Balance')
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
