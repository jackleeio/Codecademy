"""
This program create a Python class(BankAccount class) that can be used to create and manipulate a personal bank account.
And it can do the function of Accepting deposits, Allowing Withdrawals, Showing the balance, Show the details of the account.

Author: Jack Lee
"""

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "%s 's account. Balance: %.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print("%s 's account. Balance: %.2f" % (self.name, self.balance))
    
  def deposit(self, amount):
    if amount <= 0:
      print("You shouldn't deposit less than or equal to zero!")
      return
    else:
      print("%.2f is deposited Successfully!" % amount)
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount > self.balance:
      print("The money you want to withdraw is greater than the balance.")
      return
    else:
      print("%.2f is withdrawed successfully!" % amount)
      self.balance -= amount
      self.show_balance()


my_account = BankAccount("Jack")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)


