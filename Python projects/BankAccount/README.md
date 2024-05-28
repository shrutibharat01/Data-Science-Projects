# Bank Account Management System

This is a simple Bank Account Management System implemented in Python. The system allows users to create, manage, and interact with both regular bank accounts and savings accounts. The project is structured into two main files: `BankAccount.py` and `Tester.py`.

## Features

- **BankAccount**: Basic bank account functionalities including deposit, withdrawal, and transfer.
- **SavingsAccount**: Specialized bank account with additional withdrawal fees.
- **Menu-Driven Interface**: User-friendly command-line interface for interacting with accounts.
- **Error Handling**: Proper error handling for invalid operations.

## Project Structure

- `bank_module.py`: Contains the implementation of the `BankAccount` and `SavingsAccount` classes.
- `Tester.py`: Provides a menu-driven interface for users to interact with the system.

## Requirements

- Python 3.x

## Usage

1. **Run the Application**:
    ```sh
    python Tester.py
    ```

2. **Follow the Menu Instructions**:
    - **1. Create Bank Account**: Create a new regular bank account.
    - **2. Create Savings Account**: Create a new savings account.
    - **3. Deposit Money**: Deposit money into an account.
    - **4. Withdraw Money**: Withdraw money from an account.
    - **5. Transfer Money**: Transfer money between accounts.
    - **6. View Account Details**: View the details of an account.
    - **7. Exit**: Exit the application.

## Example

```sh
Bank Account Management System
1. Create Bank Account
2. Create Savings Account
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. View Account Details
7. Exit
Enter your choice: 1
Enter initial amount: 1000
Enter account name: Shruti
Account created successfully for Shruti

Enter your choice: 3
Enter account name: Shruti
Enter deposit amount: 500
Deposit successfully
New Balance: 1500.00

Enter your choice: 6
Enter account name: Shruti
Customer_id -> 0, Bank Account Name -> JohnDoe, Balance -> 1500.00

