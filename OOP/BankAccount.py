class BankAccount:
  def __init__(self, account_number, balance):
    self.account_number = account_number
    self.balance = balance

  def get_balance(self):
    balance = self.balance
    print(f"Your current balance is: ${balance}")

  def deposit(self, amount):
    self.balance += amount
    print(f"You have deposited ${amount}. Your new balance is: ${self.balance}")

  def withdraw(self, amount):
    self.balance -= amount
    print(f"You have withdrawn ${amount}. Your new balance is: ${self.balance}")

account1 = BankAccount("123456789", 1000)

# account1.get_balance()
# account1.deposit(500)
account1.withdraw(200)