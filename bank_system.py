class BankAccount:
    def __init__(self, account_holder, initial_deposit=0.0):
        self.account_holder = account_holder

        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        self._balance = initial_deposit
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")

        self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self._balance += amount
        self._transactions.append(f"Deposited: {amount}")
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        if self._balance < amount:
            raise ValueError("Insufficient balance.")

        self._balance -= amount
        self._transactions.append(f"Withdrawn: {amount}")
        return amount

    def get_transaction_history(self):
        return self._transactions.copy()

class ATM:
    def __init__(self, bank_account):
        if not isinstance(bank_account, BankAccount):
            raise TypeError("bank_account must be a BankAccount instance.")

        self._account = bank_account
        self.__pin = "1234"
        self._is_authenticated = False

    def authenticate(self, entered_pin):
        self._is_authenticated = entered_pin == self.__pin
        return self._is_authenticated

    def check_balance(self):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
        return self._account.balance

    def perform_deposit(self, amount):
        if not self._is_authenticated:
            print("Authentication required.")
            return None
        try:
            return self._account.deposit(amount)
        except ValueError as error:
            print(f"Deposit failed: {error}")
            return None

    def perform_withdrawal(self, amount):
        if not self._is_authenticated:
            print("Authentication required.")
            return None
        try:
            return self._account.withdraw(amount)
        except ValueError as error:
            print(f"Withdrawal failed: {error}")
            return None

    def print_mini_statement(self):
        if not self._is_authenticated:
            print("Authentication required.")
            return

        transactions = self._account.get_transaction_history()
        print("\n--- BANK STATEMENT ---")
        if not transactions:
            print("No transactions yet.")
        else:
            for transaction in transactions[-3:]:
                print(transaction)
        print("-" * 30)
    
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000.0)
    atm = ATM(account)

    if atm.authenticate(atm._ATM__pin):
        print(f"Previous Balance: {atm.check_balance()}")
        atm.perform_deposit(500)
        atm.perform_withdrawal(200)
        atm.perform_deposit(300)
        print(f"Current Balance: {atm.check_balance()}")
        atm.print_mini_statement()
    else:
        print("Authentication failed.")
