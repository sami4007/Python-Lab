class BankAccount:
    def __init__(self, account_no, opening_balance, opening_date, customer_name):
        self.account_number = account_no
        self.balance = opening_balance
        self.date_of_opening = opening_date
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"{amount} has been deposited successfully.")
        print(f"Available Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("Withdrawal failed. Invalid amount or insufficient funds.")
            return

        self.balance -= amount
        print(f"{amount} has been withdrawn successfully.")
        print(f"Available Balance: {self.balance}")

    def check_balance(self):
        print(f"{self.customer_name}'s Current Balance: {self.balance}")
        return self.balance


account = BankAccount("10485", 2000, "2026-08-02", "Sami")

account.check_balance()
account.deposit(8000)
account.withdraw(4000)