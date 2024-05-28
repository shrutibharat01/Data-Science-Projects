class BankException(Exception):
    pass


class BankAccount:
    counter = 0

    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        self.cid = BankAccount.counter
        BankAccount.counter += 1

    def __str__(self):
        return f'Customer_id -> {self.cid}, Bank Account Name -> {self.name}, Balance -> {self.balance:.2f}'

    def get_account_name(self):
        return self.name

    def set_account_name(self, new_val):
        self.name = new_val

    def get_balance(self):
        return self.balance

    def set_balance(self, new_val):
        if isinstance(new_val, int) or isinstance(new_val, float):
            self.balance = new_val
        else:
            raise ValueError('Invalid type')

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount
        print("Deposit successfully")
        print(f"New Balance: {self.get_balance():.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise BankException('Insufficient Balance')
        self.balance -= amount
        print('Withdraw successfully')
        print(f"New Balance: {self.get_balance():.2f}")

    def transfer(self, amount, account):
        print('Transfer Begin...')
        self.withdraw(amount)
        account.deposit(amount)
        print('Transfer complete...')


class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += (amount * 1.05)
        print('Deposit complete')
        print(f"New Balance: {self.get_balance():.2f}")


class SavingsAccount(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        total_withdrawal = amount + self.fee
        if total_withdrawal > self.balance:
            raise BankException('Insufficient Balance')
        self.balance -= total_withdrawal
        print('Withdraw successfully')
        print(f"New Balance: {self.get_balance():.2f}")
