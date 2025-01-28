# Banking System Implementation

## Features

- Account Management
  - Create checking and savings accounts
  - View account balance and type
  - Calculate interest for savings accounts

- Transaction Types
  - Deposits
  - Withdrawals 
  - Transfers between accounts
  - Interest calculations

- Transaction History
  - Track all account transactions
  - Store transaction timestamps

## Classes

### CheckingAccount
- Basic account type with deposit/withdraw functionality
- Maintains balance and username
- Validates transaction amounts

### SavingAccount
- Extends CheckingAccount
- Includes 5% interest rate
- Can calculate and add interest to balance

### Transaction
- Records all account activities
- Stores transaction details:
  - Amount
  - Balance after transaction
  - Transaction type
  - Timestamp
  - Sender/receiver for transfers

### Bank
- Main system controller
- Manages all accounts and transactions
- operations:
  - Account registration
  - Money transfers
  - Transaction history tracking
  - Total bank balance calculation

## Usage Example

```python
# Create a new bank instance
bank = Bank()

# Register accounts
bank.register("alice", 1000, "saving")
bank.register("bob", 500, "checking")

# Perform transactions
bank.deposit("bob", 200)
bank.withdraw("alice", 100)

# Calculate interest for savings account
bank.calculate_interest("alice")

bank.transfer("alice", "bob", 300)

# View transaction history
alice_transactions = bank.get_transaction_history("alice")
bob_transactions = bank.get_transaction_history("bob")

print("\ntransfer logs:\n")

for transaction in alice_transactions:
    print(transaction)
for transaction in bob_transactions:
    print(transaction)
```

output:
```
Deposited 200 to bob. New balance: 700
Withdrew 100 from alice. New balance: 900
Interest calculated: 45.0
Transferred 300 from alice to bob

transfer logs:

alice - withdraw - 100 - 900 - 2025-01-04 13:16:14.930791
alice - interest - 45.0 - 945.0 - 2025-01-04 13:16:14.931159
from: alice to: bob - transfer - amount: 300 - balance: 645.0 - 2025-01-04 13:16:14.931992
bob - deposit - 200 - 700 - 2025-01-04 13:16:14.930271
```