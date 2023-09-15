class Bank_Account:
  def __init__(self):
    self.balance=0
    print("Hello!!!Welcome to the Deposit Withdrawal Machine")
  def deposit(self):
    amount=float(input("Enter amount to be deposited:"))
    self.balance+=amount
    print("\n Amount Depostied:",amount)
  def withdraw(self):
    amount=float(input("Enter amount to be withdrawn:"))
    if self.balance>=amount:
         self.balance-=amount 
         print("\n You withdrew:",amount)
    else: 
         print("\n Insufficient balance")
  def display(self):
    print("\n Net Available Balance=",self.balance)
s=Bank_Account()
s.deposit()
        
