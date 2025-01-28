import datetime

class CheckingAccount:
    def __init__(self, username, balance):
        self.balance = balance
        self.username = username
        self.type = "checking"

    def get_balance(self) -> int:
        return self.balance
    
    def deposit(self,amount) -> int | None:
        if amount > 0:
            self.balance += amount
            return amount
        else:
            print("invalid amount")
            return None

    def withdraw(self,amount) -> int | None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print("you don't have enough balance")
            return None

class SavingAccount(CheckingAccount):
    def __init__(self, username, balance):
        super().__init__(username, balance)
        self.type = "saving"
        self.interest_rate = 0.05
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest
    
class Transaction:
    def __init__(self, account, amount, balance, transaction_type, receiver_account = None):
        self.account = account
        self.amount = amount
        self.balance = balance
        self.transaction_type = transaction_type

        if (transaction_type == "transfer"):
            if receiver_account is not None:
                self.receiver_account = receiver_account
            else:
                raise Exception("receiver account is required for transfer")
            
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        if (self.transaction_type == "transfer"):
            return f"from: {self.account.username} to: {self.receiver_account.username} - {self.transaction_type} - amount: {self.amount} - balance: {self.balance} - {self.timestamp}"
        else:
            return f"{self.account.username} - {self.transaction_type} - {self.amount} - {self.balance} - {self.timestamp}"

class Bank:
    def __init__(self):
        self.accounts: dict[str, CheckingAccount | SavingAccount] = {}
        self.transactions: list[Transaction] = []
    
    def register(self, username, initial_balance, type):
        if username in self.accounts:
            print("username already exists")
            return None
        else:
            if type == "saving":
                account = SavingAccount(username, initial_balance)
                self.accounts[username] = account
                return account
            elif type == "checking":
                account = CheckingAccount(username, initial_balance)
                self.accounts[username] = account
                return account
            return None
        
    def get_account(self, username):
        if username in self.accounts:
            return self.accounts[username]
        else:
            print("username not found")
            return None
    
    def deposit(self, username, amount):
        account = self.get_account(username)
        if account:
            result = account.deposit(amount)
            if result:
                transaction = Transaction(account, amount, account.get_balance(), "deposit")
                self.transactions.append(transaction)
                print(f"Deposited {amount} to {username}. New balance: {account.get_balance()}")
            else:
                print("invalid amount")
        else:
            print("username not found")
    
    def withdraw(self, username, amount):
        account = self.get_account(username)
        if account:
            result = account.withdraw(amount)
            if result:
                transaction = Transaction(account, amount, account.get_balance(), "withdraw")
                self.transactions.append(transaction)
                print(f"Withdrew {amount} from {username}. New balance: {account.get_balance()}")
            else:
                print("you don't have enough balance")
        else:
            print("username not found")

    def get_transaction_history(self, username):
        account = self.get_account(username)
        if account:
            transactions = [transaction for transaction in self.transactions if transaction.account == account]
            return transactions
        else:
            print("username not found")
            return None
        
    def get_account_balance(self, username):
        account = self.get_account(username)
        if account:
            return account.get_balance()
        else:
            print("username not found")
            return None
        
    def get_account_type(self, username):
        account = self.get_account(username)
        if account:
            return account.type
        else:
            print("username not found")
            return None
        
    def calculate_interest(self, username):
        account = self.get_account(username)
        if account and account.type == "saving":
            interest = account.calculate_interest()
            transaction = Transaction(account, interest, account.get_balance(), "interest")
            self.transactions.append(transaction)
            print(f"Interest calculated: {interest}")
        else:
            print("Invalid account type or account not found")
    
    def transfer(self, sender_username, receiver_username, amount):
        sender_account = self.get_account(sender_username)
        receiver_account = self.get_account(receiver_username)

        if sender_account and receiver_account:
            if sender_account.withdraw(amount):
                receiver_account.deposit(amount)
                transaction = Transaction(sender_account, amount, sender_account.get_balance(), "transfer", receiver_account)
                self.transactions.append(transaction)
                print(f"Transferred {amount} from {sender_username} to {receiver_username}")
            else:
                print("Insufficient balance in the sender's account")
        else:
            print("Invalid sender or receiver username")

    def get_total_balance(self):
        total_balance = sum(account.get_balance() for account in self.accounts.values())
        return total_balance
    

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

for transaction in alice_transactions:
    print(transaction)
for transaction in bob_transactions:
    print(transaction)