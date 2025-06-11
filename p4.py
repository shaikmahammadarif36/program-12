class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    def get_account_number(self):
        return self._account_number
    def get_balance(self):
        return self._balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount for deposit.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")
account = BankAccount("1234567890", 1000)
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())
account.deposit(500)
account.withdraw(200)
account._account_number = "9876543210"
account._balance = 5000  
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())
