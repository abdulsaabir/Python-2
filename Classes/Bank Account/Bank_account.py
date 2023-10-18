
class BankAccount:
    def __init__(self, owner_name, amount):
        # Initialize the account owner's name and balance
        self.account_owner = owner_name
        self.balance = amount

    def get_balance(self):
        # Prompt for the user's name
        user = input('To See Your Balance Please Enter Your Name: ')
        
        # Check if the entered name matches the account owner's name
        if user == self.account_owner:
            print(f"Account balance: {self.balance}") 
        else:
            # Inform the user that they are not the account owner
            print('Invalid user. You are not the account owner.')

    def withdraw(self):
        # Prompt for the user's name
        user = input('Enter The name of Withdrawal: ')
        # Check if the entered name matches the account owner's name

        if user == self.account_owner:
            # Prompt for the withdrawal amount
            amount = input('Enter The amount : ')  

            # Check if the withdrawal amount is less than or equal to the account balance
            if int(amount) <= self.balance:
                # Deduct the withdrawal amount from the account balance
                self.balance -= int(amount)  
            else:
                # Inform the user that there's insufficient balance for the withdrawal
                print("Insufficient balance")
        
        else:
            # Inform the user that they are not the account owner
            print('Invalid user. You are not the account owner.')

# Create a BankAccount instance with an owner name "suheyba ahmed" and an initial balance of 1000
account = BankAccount("suheyb", 1000)

# look at the balance
account.get_balance()

# withdraw Money
account.withdraw()

# Check again the balance
account.get_balance()




