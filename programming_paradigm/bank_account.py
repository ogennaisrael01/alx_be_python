# A simple bank account 

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance =  account_balance

    def deposit(self, amount):
        """
        A method to deposit to account
        """
        try:
            if amount <= 0:
                return False
            else:
                self.account_balance += amount
        except ValueError:
            print(f"Error: Invalid amount {amount}. Please enter a positive number.")

    def withdraw(self, amount):
        """
        A method to withdraw from accoount
        """  
        try: 
            if amount <= 0:
                return False
            if amount > self.account_balance:
                return False
            else:
                self.account_balance -= amount
                return True
        except ValueError as e:
            print(f"Error: {e}")

    def display_balance(self):
        """"
        A method to display the current balance
    """
        print(f"Current Balance: ${self.account_balance:.2f}")