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

# Example usage
if __name__ == "__main__":
    cc = CreditCard("Bank of Python", "1234567890123456", "123 Python St", 1000.0)
    cw = CryptoWallet("1A2b3C4d5E6f7G8h9I0j", 2.5)  # Balance in BTC

    print(cc)
    print(cw)

    make_payment(cc, 150.0)  # Using CreditCard
    make_payment(cw, 0.5)    # Using CryptoWallet

    print(f"Remaining CreditCard Balance: ${cc.balance}")
    print(f"Remaining CryptoWallet Balance: {cw.balance} BTC")

# Another example usage:

payment_queue = [
    CreditCard("Bank A", "1111222233334444", "456 Java Ave", 500.0),
    CryptoWallet("3F4g5H6i7J8k9L0m1N2o", 1.0),
    CreditCard("Bank B", "5555666677778888", "789 C# Blvd", 300.0),
    CryptoWallet("4G5h6I7j8K9l0M1n2O3p", 0.75),
    CreditCard("Bank C", "9999000011112222", "101 Swift St", 800.0)
]

for method in payment_queue:
    method.process_payment(amount=100 if isinstance(method, CreditCard) else 0.1)
    print(f"Updated Balance: {method.balance if isinstance(method, CreditCard) else method.balance} {'USD' if isinstance(method, CreditCard) else 'BTC'}")
