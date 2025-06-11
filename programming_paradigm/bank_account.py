# A simple bank account 

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        """"
        A method to deposit to acoount
        """
        if amount <= 0:
            return False
        else:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        A method to withdraw from accoount
        """
        if not amount:
            return False   
        if amount < self.account_balance:
           print("Insufficient funds.") 
        self.account_balance -= amount
        return True
       
    def display_balance(self):
        print(f"Current Balance: {self.account_balance}.")