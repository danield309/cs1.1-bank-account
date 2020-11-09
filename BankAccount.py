class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount}") 
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount withdrawn: ${amount}")
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10