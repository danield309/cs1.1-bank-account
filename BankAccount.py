# bank account class
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    # deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount}") 
   
    # withdraw method
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount withdrawn: ${amount}")
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
    
    # balance method
    def get_balance(self):
        print(f"Balance: ${self.balance}")
  
    # add interest method
    def add_interest(self):
        balance = self.balance
        interest = balance * 0.00083
        self.balance = self.balance + interest
   
    # print receipt method
    def print_receipt(self):
        stars = []

        for i in str(self.account_number):
            stars.append("*")
        hide_accountnum = str(self.account_number)
        stars[len(stars)-1] = hide_accountnum[len(stars)-1]
        stars[len(stars)-2] = hide_accountnum[len(stars)-2]
        stars[len(stars)-3] = hide_accountnum[len(stars)-3]
        stars[len(stars)-4] = hide_accountnum[len(stars)-4]

        acc_stars = ""
        acc_stars = acc_stars.join(stars)
        
        print(self.full_name)
        print(f"Account No.: {acc_stars}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Balance: {self.balance}")

# bank account 1
daniel_account = BankAccount("Daniel Duque", 490281789, 1982331, 7000)
daniel_account.deposit(5000)
daniel_account.print_receipt()

# bank account 2
travis_account = BankAccount("Travis Scott", 914253880, 8982331, 5300)
travis_account.get_balance()
travis_account.withdraw(5301)
travis_account.print_receipt()

# bank account 3
aubrey_account = BankAccount("Aubrey Graham", 666666666, 7982331, 100000)
aubrey_account.add_interest()
aubrey_account.print_receipt()

