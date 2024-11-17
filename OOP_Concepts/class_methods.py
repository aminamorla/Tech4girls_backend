class BankAccount:
    # Class variable
    bank_name = "Tech4Girls Bank"

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:
            self.balance += amount
            print(f'Deposited ${amount}. New balance is ${self.balance}.')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrew ${amount}. New balance is ${self.balance}.')
            else:
                print('Insufficient balance!')
        else:
            print('Withdrawal amount must be positive.')

    @staticmethod
    def bank_policy():
        # Static method to display the bank policy
        print('Bank policy: We are committed to providing secure, reliable, and efficient banking services to all our customers.')

    @classmethod
    def get_bank_name(cls):
        # Class method to return the bank name
        return cls.bank_name

# This block will run only when the script is executed directly (not imported)
if __name__ == "__main__":
    # Create a bank account for Amina
    amina_account = BankAccount("Amina")

    # Deposit money into Amina's account
    amina_account.deposit(2000)

    # Withdraw money from Amina's account
    amina_account.withdraw(1000)  # Fixed typo here

    # Try withdrawing an amount larger than the balance
    amina_account.withdraw(1500)

    # Call static method
    BankAccount.bank_policy()

    # Call class method
    print(f'Bank name: {BankAccount.get_bank_name()}')

    #create another bank account for Yarauta
    yarauta_account = BankAccount('Yarauta')
    yarauta_account.deposit(5000)
    yarauta_account.withdraw(2000)
    print(f'Bank name: {yarauta_account.get_bank_name()}')















        



        