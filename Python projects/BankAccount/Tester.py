from BankAccount import *


def find_ac_by_name(accounts, name):
    for account in accounts:
        if account.get_account_name() == name:
            return account
    return None


def main():
    accounts = []

    while True:
        print("\n Bank Account Management System")
        print("1. Create Bank Account")
        print("2. Create Savings Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. View Account Details")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                initial_amount = float(input("Enter initial amount: "))
                acct_name = input("Enter account name: ")
                account = BankAccount(initial_amount, acct_name)
                accounts.append(account)
                print(f"Account created successfully for {account.get_account_name()}")

            case 2:
                initial_amount = float(input("Enter initial amount: "))
                acct_name = input("Enter account name: ")
                account = SavingsAccount(initial_amount, acct_name)
                accounts.append(account)
                print(f"Savings account created successfully for {account.get_account_name()}")

            case 3:
                acct_name = input("Enter account name: ")
                amount = float(input("Enter deposit amount: "))
                account = find_ac_by_name(accounts, acct_name)
                if account:
                    try:
                        account.deposit(amount)
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Account not found")

            case 4:
                acct_name = input("Enter account name: ")
                amount = float(input("Enter withdrawal amount: "))
                account = find_ac_by_name(accounts, acct_name)
                if account:
                    try:
                        account.withdraw(amount)
                    except BankException as e:
                        print(f"Error: {e}")
                else:
                    print("Account not found")

            case 5:
                from_acct_name = input("Enter your account name: ")
                to_acct_name = input("Enter recipient's account name: ")
                amount = float(input("Enter transfer amount: "))
                from_account = find_ac_by_name(accounts, from_acct_name)
                to_account = find_ac_by_name(accounts, to_acct_name)
                if from_account and to_account:
                    try:
                        from_account.transfer(amount, to_account)
                    except BankException as e:
                        print(f"Error: {e}")
                else:
                    print("Account not found")

            case 6:
                acct_name = input("Enter account name: ")
                account = find_ac_by_name(accounts, acct_name)
                if account:
                    print(account)
                else:
                    print("Account not found")

            case 7:
                print("Exiting...")
                break

            case _:
                print("Invalid choice. enter again.")


if __name__ == "__main__":
    main()
