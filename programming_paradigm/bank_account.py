'''
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.

'''

class BankAccount:
    def __init__(self , account_balance  = 0):
        self.account_balance = account_balance
    def deposit(self,amount):
        self.account_balance+= amount

    def withdraw(self , amount):
        if self.account_balance - amount >= 0:
            self.account_balance -= amount
            return True
        else: return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

