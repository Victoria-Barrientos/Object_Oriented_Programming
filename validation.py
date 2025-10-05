# Builds on encapsulation to add input validation.
# Validates credit card number (13–19 digits).
# 👉 Expected outcome: User creation should succeed only with valid input, and balance updates should never allow negatives.

class PersonaWithoutValidation:
    def __init__(
            self,
            name: str,
            email: str,
            bank: str,
            card_number: str,
            billing_address: str,
            balance: float
        ):
        self.name = name
        self.email = email
        self.bank = bank 
        self.__card_number = card_number
        self.__billing_address = billing_address
        self.__balance = balance

    def __str__(self):
        return f"""
        Name: {self.name}
        Email: {self.email}
        Bank: {self.bank}
        Card Number: {self.__card_number}
        Billing Address: {self.__billing_address}
        Balance: ${self.__balance}
        """

class PersonaWithValidation:
    """
    Applying encapsulation principles -> Getters and Setters
    """
    def __init__(
            self,
            name: str,
            email: str,
            bank: str,
            card_number: str,
            billing_address: str,
            balance: float
        ):
        if card_number.isdigit() and 13 <= len(card_number) <= 19:
            self.__card_number = card_number
            self.name = name
            self.email = email
            self.bank = bank
            # Safe guard card_number as a private attribute ==> __card_number       
            self.__card_number = card_number
            self.__billing_address = billing_address
            self.__balance = balance
        else:
            raise ValueError("Card number must be between 13 and 19 digits, all numeric. User creation failed.")
    
    @property #Getter
    def Balance(self):
            return self.__balance
        
    @Balance.setter #Setter
    def Balance(self, value):
        if (value > 0):
            self.__balance = value
            print(f"Your new balance is: ${self.__balance}")
        else:
            raise ValueError("Balance cannot be negative")
