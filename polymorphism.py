# In this example, we define two different payment method classes: CreditCard and CryptoWallet.
# Both classes implement a process_payment method, demonstrating polymorphism.

class CreditCard:
    def __init__(self, bank, card_number, billing_address, balance):
        self.bank = bank
        self.card_number = card_number
        self.billing_address = billing_address
        self.balance = balance

    def __str__(self):
        return f"CreditCard(Bank: {self.bank}, Card Number: {self.card_number}, Billing Address: {self.billing_address})"
    
    def process_payment(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Processing payment of ${amount} using card {self.card_number} from {self.bank}")
        else:
            print("Insufficient funds or invalid amount")

class CryptoWallet:
    def __init__(self, wallet_address, balance):
        self.wallet_address = wallet_address
        self.balance = balance

    def __str__(self):
        return f"CryptoWallet(Address: {self.wallet_address}, Balance: {self.balance} BTC)"
    
    def process_payment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Processing crypto payment of {amount} BTC from wallet {self.wallet_address}")
        else:
            print("Insufficient balance in crypto wallet")

# Function to process payment using any payment method
def make_payment(payment_method, amount):
    payment_method.process_payment(amount)